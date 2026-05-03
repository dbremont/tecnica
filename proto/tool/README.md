# Meta Tool Spec

> An **epistemic tool** is any technique, method, or formal mechanism used by an observer to construct, represent, and validate descriptions of reality.

> Take a **specific epistemic tool** `"(tool - note)"` and design a **web-based interactive notebook** whose purpose is to systematically support a human in **understanding, interrogating, and operationalizing** that tool.

> Our goal is to create a  **Interactive Epistemic Notebook**: a controlled experimental environment for epistemic tools, where understanding is achieved through structured interaction with the tool’s formal, computational, and behavioral structure.

Non-Functional Requirements:

* **Cognitive Clarity**
  The interface must minimize ambiguity and reduce cognitive load while preserving formal precision.

* **Progressive Disclosure**
  Complexity should be revealed incrementally (from intuition → formalism → edge cases).

* **Interactivity Latency**
  All interactions (parameter changes, simulations) must respond in near real-time.

* **Determinism & Reproducibility**
  All outputs must be reproducible given the same inputs and parameters.

* **Epistemic Transparency**
  Assumptions, limitations, and transformation logic must be explicitly exposed.

* **Modularity**
  Components (visualizations, simulations, explanations) should be composable and independently testable.

* **Observability**
  Internal states (intermediate variables, transformations) should be inspectable.

Functional Requirements:

* **Conceptual Layer**

  * Provide minimal and precise definitions of the tool
  * Explicitly state the epistemic role and scope

## Interaction Layer

> ...

* **Purpose**
  The interaction layer defines how the user **engages with the epistemic structure** of the tool through controlled, observable manipulations.

* **Core Principle**
  Interaction is not for exploration alone, but for **structured epistemic intervention**: every action should reveal how the tool transforms inputs into outputs.

* **Components**

  * **Parameter Controls**
    Sliders, inputs, and selectors to modify the tool’s defining variables
  * **Execution Controls**
    Step, run, pause, and reset mechanisms for procedural inspection
  * **State Inspection**
    Direct access to intermediate states and internal variables
  * **Linked Views**
    Synchronized visualizations (e.g., input space ↔ transformation ↔ output artifact)
  * **Constraint Injection**
    Ability to enforce or violate assumptions deliberately

* **Design Constraints**

  * All interactions must produce **immediate, interpretable changes**
  * The mapping between action → transformation → artifact must be **explicit**
  * Hidden state is minimized; internal dynamics are **externally visible**

### Objective

* Our main goal is to construct a **set of interactive tools** that enable a human to:

  * **Interrogate** the epistemic tool
    (What does it actually compute? Under what assumptions?)

  * **Manipulate** its structure
    (How do parameter changes alter the transformation?)

  * **Observe** its behavior
    (How does the output evolve under different inputs and conditions?)

  * **Diagnose** its limits
    (When does it fail, and why?)

  * **Internalize** its mechanism
    (Develop a correct mental model of its operational logic)

### Outcome

The interaction layer should transform passive understanding into **active epistemic control**:

> The user should be able not only to *use* the tool, but to **predict its behavior, detect its failure modes, and reason about its outputs before execution**.

## Technology Stack

* HTML
* CSS
* JS
* No Frameworks, Like React
* Can Used Libraries - But Be Minimalistic.

## References

* [Epistemic Tool Template](https://www.notion.so/Epistemic-Tool-Template-2e5c0f5171ec800fa9caf91bb16bcab9?source=copy_link)
