# Ember.js
  
> **Ember.js** is an open-source JavaScript framework designed for building **ambitious web applications**. It emphasizes **convention over configuration**, enabling developers to be highly productive with a well-structured, opinionated architecture.
> 

> A Note on Modern **Ember.js**.
> 

### 🧭 When to Use Ember.js?

**Ideal for:**

- Large-scale applications
- Teams that benefit from strong conventions
- Long-lived, maintainable codebases
- Projects needing strong routing and state management

## Index

## QA

- …

## Install

```bash
npm install -g ember-cli
ember new helloworld
cd helloworld

...

ember serve
```

## Ember APP

> Note: This is the core conceptual abstraction in order to understand Ember JS.
> 

> An **Ember.js** application, in a **very technical sense**, is a **client-side JavaScript application framework** built around the **Model-View-ViewModel (MVVM)** architectural pattern, emphasizing **convention over configuration**, **reactive data flow**, and **URL-driven application state**.
> 

> **Ember CLI**:  App Description → App (Browser).
> 

## 🔧 Core Concepts

- **Ember CLI**: The command-line tool for scaffolding, building, testing, and serving Ember apps. It enforces project structure and best practices.
- **Convention over Configuration**: You follow Ember’s conventions and get productivity gains—less boilerplate and more coherence.
- **Ember Data**: A powerful data persistence library that helps manage models and works well with JSON:API or custom backends.
- **Handlebars Templates**: Uses Handlebars.js for declarative HTML rendering. It's easy to bind values and conditionally render elements.
- **Routing**: One of Ember's strongest points. Its router is state-aware and supports nested routes, dynamic segments, query params, and loading/substates.
- **Components**: Reusable, isolated pieces of UI logic. Ember Octane (modern Ember) favors Glimmer components (lightweight, fast).
- **Services**: Long-lived objects for shared state or behavior (e.g., authentication, notifications).

## 📘 Versions

| Version Range | Era Name | Years Active | Key Features & Changes | Notable Limitations/Transitions |
| --- | --- | --- | --- | --- |
| **1.x** | **Classic Ember** | 2011–2015 | - `Ember.View`, `Ember.Controller`- Two-way data binding- Early Ember Data- Handlebars templates | - Verbose `get/set` syntax- Coupled logic and view- Pre-CLI era |
| **2.x** | **Modernization Phase** | 2015–2018 | - First-class components (`Ember.Component`)- Services- One-way data flow- Better routing | - Still used `Ember.Object.extend`- `Controller` still prominent |
| **3.x** | **Toward Modern Ember** | 2018–2020 | - Native JS classes- Decorators preview (`@tracked`, `@action`)- Glimmer VM rewrite | - Still allowed classic patterns- Transition not yet enforced |
| **4.x** | **Octane Era** | 2020–2023 | - Glimmer components- Full decorator support- Strict templates- Angle bracket invocation | - Classic components deprecated- Learning curve shift |
| **5.x** | **Stability & Refinement** | 2023–Present | - RFC-driven evolution- Template imports (proposed)- TypeScript-ready- Minimal runtime experiments | - Codemods for old syntax- Migration from Octane still required |

## 🚀 Modern Ember (a.k.a. Ember Octane)

Introduced modern JavaScript features:

- **Native classes**
- **Tracked properties** for reactivity
- **Glimmer components** (lightweight and faster rendering engine)
- **Modifiers** for low-level DOM behavior

## 📦 Ecosystem & Tooling

- **Addons**: Ember has a large addon ecosystem.
- **Testing**: Testing is built-in (QUnit by default), with support for unit, integration, and acceptance testing.
- **Build system**: Ember CLI uses Broccoli.js under the hood.

## Browser-Server Interaction

**Ember.js runs entirely in the browser** — it is a **client-side JavaScript framework**. Here’s a breakdown of **how and where computation happens**:

### ✅ What Ember Does in the **Browser** (Client-Side)

- **Routing**: Ember uses `ember-router` to manage URLs and navigate between pages without full page reloads.
- **Rendering**: Glimmer (Ember’s rendering engine) builds and updates the DOM using declarative templates and reactive state.
- **State Management**: Tracked properties and component state live in the browser.
- **User Interaction**: Handling of clicks, forms, inputs, animations — all done in JavaScript.
- **Templating & Logic**: Handlebars templates + components run entirely client-side.
- **Data Fetching**: Uses `fetch()` or Ember Data (`store.findRecord`, etc.) to make HTTP calls to an API server.
- **Client-Side Validation**: Form input validation can happen before sending data to a backend.

### 🔄 How Ember Communicates With the Server

Via **AJAX/HTTP APIs**

- Ember does not include its own backend — you can connect it to **any backend** (Rails, Node.js, Java, etc.).
- You typically use:
    - **Ember Data** (ORM-like layer) to fetch/save models
    - Or `fetch()` / `axios` directly
- Backend only supplies **data (JSON)**; Ember renders the UI.

## **Build and Packaging System**

### ➤ **Broccoli + Ember CLI**

- **Ember CLI**: Standardized project and build tool; supports:
    - Asset pipeline (Broccoli.js)
    - Addon ecosystem
    - ES6 module transpilation via Babel
- **Addon system**: True **meta-packages**—can inject files, extend build pipeline, and modify application runtime.

### ➤ **Modules & Namespacing**

- Uses ES6 module system (post-Ember 3.x) with strict conventions (`app/components/`, `app/routes/`, etc.)
- Dynamic resolver: Infers class/function lookups from file path patterns.

## FastBoot

> …
> 

## App Analytics

> User Analytics, …
> 
- [ ]  
- [ ]  https://github.com/PostHog/posthog
- [ ]  https://github.com/openreplay/openreplay/
- [ ]  https://github.com/adopted-ember-addons/ember-metrics
- [ ]  https://github.com/rrweb-io/rrweb
- [ ]  [UI Analytics](https://www.notion.so/UI-Analytics-16ec0f5171ec808286ecdc67493f9ea3?pvs=21)

## Debugging

> `ember serve --devtools-port=9229`
> 

## Addons

- [ ]  https://emberobserver.com/

## Tooling

🔍 **Ember Inspector (Browser DevTools Extension)**

🧭 **Route Tracing & Transitions**

🧬 **Tracked Property Debugging**

📉 **Performance Analysis**

## Case Studies

- [ ]  https://github.com/ember-learn/super-rentals

## References

- https://en.wikipedia.org/wiki/Ember.js
- https://www.thesoftwaresimpleton.com/
- https://github.com/csiglab/cstudies/blob/main/src/discourse.md
- https://cli.emberjs.com/release/
- https://guides.emberjs.com/release/ember-inspector/
- https://emberjs.com/
- https://glimmerjs.com/
