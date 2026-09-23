# Role Library — Natural-Language Router

The skill router is the plain-English front door to the library: describe the task and it returns ranked role assemblies (role skill + suggested capabilities + suggested integrations), each with operating-contract elements. It selects contracts; it never grants authority. Ships with its own matcher script and index data so it works standalone — install it together with whichever domain packs you need.

**Contents:** 1 skill(s).

## Skills

- `skill-router`

## Install

```
/plugin install role-library-router
```

## License

Licensing is pending the library owner's decision. See `LICENSE and COMMERCIAL-LICENSE.md` in the repo root — do not redistribute commercially until real license text ships.

## Why a separate plugin
The router is cross-cutting infrastructure, not domain content: it references all 202 entries but belongs to none. Packaging it separately means a user can install just the router plus one domain pack and get full natural-language routing. Bundling it inside a domain pack would force an arbitrary domain choice on every user.
