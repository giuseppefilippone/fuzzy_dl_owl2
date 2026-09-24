# Summary

An abstract base class equips description-logic concepts with a uniform way to store, read, and update the role (binary relation) they are associated with.

## Description

In the fuzzydl framework, concepts such as existential or universal restrictions quantify over a role, so many concept implementations need a shared, reusable mechanism for holding that role name. **HasRoleInterface** supplies exactly that: its constructor accepts a role string and stores it in a private attribute, while a property pair exposes read and write access so the role can be inspected or replaced at any point during the object's lifetime. The design is intentionally minimal — no runtime type checking or validation is performed, and the constructor's type hint is advisory only — which keeps the mixin lightweight and imposes no behavioural constraints on the classes that inherit it beyond the storage contract itself. By centralising this small piece of state management, the interface eliminates duplicated boilerplate across every role-bearing concept and guarantees that all such concepts interact with their role through one consistent API.
