#!/usr/bin/env python3
"""Natural-language router for the Agentic AI Role Library (196 entries).

Usage: route.py "write a press release for the new album" [--top N]

Returns ranked role assemblies: role skill + suggested capabilities + suggested
integrations, scored by keyword overlap with the natural-language query.
Abbreviations stay as stable IDs; the router is the natural-language interface.
"""
import json, os, re, sys, argparse
from collections import Counter

BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data")
STOP = set("""a an the and or to of in on for with as at by is are be was were it its this that these those you your we our they their he she him her i me my we us do does did not no not from into over under between through during about than then when where what which who how why can could should would will may might must have has had having been being there here all any each every both few more most other some such own same so if but up out off again once here than too very can just don use using used also within via per""".split())

def tokens(s):
    return [t for t in re.findall(r"[a-z][a-z\-]{2,}", (s or "").lower()) if t not in STOP]

def load():
    roles = json.load(open(os.path.join(BASE, "role-skills.json")))
    caps = json.load(open(os.path.join(BASE, "capability-skills.json")))
    ints = json.load(open(os.path.join(BASE, "integrations.json")))
    return roles, caps, ints

def doc_text(role):
    return " ".join([
        role.get("name", ""), role.get("description", ""), role.get("use_cases", ""),
        role.get("capability_text", ""), role.get("integrations", ""),
        role.get("output", ""), role.get("domain", ""), role.get("operating_class", ""),
    ])

def cap_text(cap):
    return " ".join([cap.get("name", ""), cap.get("what_it_does", ""),
                      cap.get("common_roles", ""), cap.get("category", "")])

def score(query_tokens, text_tokens):
    q = Counter(query_tokens); t = Counter(text_tokens)
    return sum(min(q[w], t[w]) for w in q if w in t)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("query")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    roles, caps, ints = load()
    cap_by_id = {c["skill_id"]: c for c in caps}
    int_by_id = {i["integration_id"]: i for i in ints}
    qt = tokens(a.query)
    ranked = []
    for r in roles:
        s = score(qt, tokens(doc_text(r)))
        # small boost for domain/name matches
        nm = tokens(r.get("name", "")) + tokens(r.get("domain", ""))
        s += 0.5 * score(qt, nm)
        if s > 0:
            ranked.append((s, r))
    ranked.sort(key=lambda x: -x[0])
    out = []
    for s, r in ranked[:a.top]:
        out.append({
            "role_id": r["role_id"], "role_name": r["name"],
            "role_skill_dir": "skills/" + r.get("slug", ""),
            "description": r["description"],
            "gate": r.get("gate", ""), "handoff": r.get("handoff", ""),
            "score": round(s, 2),
            "capabilities": [
                {"skill_id": cid, "name": cap_by_id[cid]["name"],
                 "skill_dir": "skills/skl-capabilities/" + cap_by_id[cid].get("slug", "")}
                for cid in r.get("suggested_skill_ids", []) if cid in cap_by_id],
            "integrations": [
                {"integration_id": iid, "name": int_by_id[iid]["name"]}
                for iid in r.get("suggested_integration_ids", []) if iid in int_by_id],
        })
    # also top standalone capabilities for the query
    cr = []
    for c in caps:
        s = score(qt, tokens(cap_text(c)))
        if s > 0: cr.append((s, c))
    cr.sort(key=lambda x: -x[0])
    for s, c in cr[:3]:
        out.append({"skill_id": c["skill_id"], "role_name": None,
                    "capability_name": c["name"], "what_it_does": c.get("what_it_does",""),
                    "score": round(s, 2)})
    if a.json:
        print(json.dumps(out, indent=1))
    else:
        for e in out:
            if e.get("role_id"):
                print(f"[{e['score']}] ROLE {e['role_id']} — {e['role_name']}")
                print(f"    {e['description']}")
                if e["capabilities"]:
                    print("    Capabilities: " + ", ".join(
                        f"{c['skill_id']} {c['name']}" for c in e["capabilities"]))
                if e["integrations"]:
                    print("    Integrations: " + ", ".join(
                        f"{i['integration_id']} {i['name']}" for i in e["integrations"]))
                print(f"    Gate: {e['gate']} | Handoff: {e['handoff']}")
            else:
                print(f"[{e['score']}] CAPABILITY {e['skill_id']} — {e['capability_name']}")
                print(f"    {e['what_it_does']}")

if __name__ == "__main__":
    main()
