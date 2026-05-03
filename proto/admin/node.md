# Node Spec

> Let's see how this

- Reality
- Action Interface & Actuation
- Concrete Technical Artifact (Technical Object)
- Technical Blueprint
- Technical Agent
- Technical Process (Activity)
- Technical Standard
- Technical Constraint
- Technical Infrastructure
- Technical Feedback
- Technical Act
- Technical Principle
- Technical Strategy
- Technical Framework
- Technical Operator
- Production Technical Object
- Constitutive Technical Object
- Technique
- Operative Technique
- Constitutive Technique
- Technical Purpose
- Technical Function
- Technical Architecture
- Technical Specification
- Technical Evolution
- Technical Labor
- Technical Institution
- Technical Research
- Technical Competence
- Technical Failure
- Technical Requirement
- Verification
- Maintenance
- Security
- Resource
- Technical Obsolescence

be catpure by the followign `schema`

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://example.org/technical-practice-node.schema.json",
  "title": "Technical Practice Node Schema",
  "description": "Schema for representing concepts that constitute technical practice (Philosophia Artium Technicarum et Operis), enabling modeling of agentic operations, artifacts, processes, and their interrelations.",
  "type": "object",
  "required": [
    "id",
    "name",
    "category",
    "inheritanceLevel",
    "description",
    "functionalRoles",
    "realityDomains",
    "historicalContext",
    "specific",
    "relationships",
    "metadata"
  ],
  "properties": {
    "id": {
      "type": "string",
      "description": "Unique identifier for the node."
    },
    "name": {
      "type": "string",
      "description": "Canonical name of the technical concept."
    },
    "category": {
      "type": "string",
      "enum": [
        "Reality",
        "ActionInterfaceAndActuation",
        "ConcreteTechnicalArtifact",
        "TechnicalBlueprint",
        "TechnicalAgent",
        "TechnicalProcess",
        "TechnicalStandard",
        "TechnicalConstraint",
        "TechnicalInfrastructure",
        "TechnicalFeedback",
        "TechnicalAct",
        "TechnicalPrinciple",
        "TechnicalStrategy",
        "TechnicalFramework",
        "TechnicalOperator",
        "ProductionTechnicalObject",
        "ConstitutiveTechnicalObject",
        "Technique",
        "OperativeTechnique",
        "ConstitutiveTechnique",
        "TechnicalPurpose",
        "TechnicalFunction",
        "TechnicalArchitecture",
        "TechnicalSpecification",
        "TechnicalEvolution",
        "TechnicalLabor",
        "TechnicalInstitution",
        "TechnicalResearch",
        "TechnicalCompetence",
        "TechnicalFailure",
        "TechnicalRequirement",
        "Verification",
        "Maintenance",
        "Security",
        "Resource",
        "TechnicalObsolescence"
      ],
      "description": "Ontological classification of the node within the technical practice framework."
    },
    "layer": {
      "type": "string",
      "enum": [
        "Problem Space",
        "Capability Space",
        "Execution Space",
        "Artifact Space",
        "Governance Space",
        "Evolutionary Space"
      ],
      "description": "Macro layer representing the primary operational stratum in which the technical concept functions. Problem Space captures requirements, purposes, constraints, and desired states that initiate technical practice. Capability Space captures agents, competencies, techniques, resources, and infrastructural capacities enabling intervention. Execution Space captures situated acts, operators, operative techniques, processes, and real-time transformations performed on reality. Artifact Space captures blueprints, specifications, constitutive components, production objects, architectures, and functional structures generated or manipulated through technical practice. Governance Space captures standards, principles, security regimes, institutions, verification systems, and regulatory structures that constrain, validate, and coordinate technical operation. Evolutionary Space captures technical research, obsolescence, historical progression, innovation trajectories, and long-term transformation of technical systems over time."
    },
    "inheritanceLevel": {
      "type": "integer",
      "minimum": 0,
      "description": "Depth within conceptual or taxonomic inheritance hierarchy."
    },
    "description": {
      "type": "string",
      "description": "Formal description of the technical concept."
    },
    "longDescription": {
      "type": "string",
      "description": "Extended technical exposition providing deeper operational, historical, and epistemic detail."
    },
    "functionalRoles": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Primary functional roles served by this node within technical practice."
    },
    "realityDomains": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "description": "Domains of reality or systems in which this node operates."
    },
    "historicalContext": {
      "type": "object",
      "required": ["summary", "chronology"],
      "properties": {
        "summary": {
          "type": "string"
        },
        "chronology": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["year", "event", "associatedContext"],
            "properties": {
              "year": { "type": "number" },
              "event": { "type": "string" },
              "associatedContext": { "type": "string" }
            },
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    },
    "specific": {
      "type": "object",
      "description": "Category-specific extension fields."
    },
    "relationships": {
      "type": "array",
      "description": "Typed edges connecting this node to others.",
      "items": {
        "type": "object",
        "required": ["relationshipType", "targetNodeId", "description"],
        "properties": {
          "relationshipFamily": {
            "type": "string",
            "enum": [
              "TeleologicalAndFunctional",
              "GenerativeAndStructural",
              "AgenticAndOperative",
              "NormativeAndRegulative",
              "EvaluativeAndCorrective",
              "StrategicAndContextual",
              "TemporalAndEvolutionary",
              "ConstitutiveAndMereological"
            ],
            "description": "High-level family of the relationship."
          },
          "relationshipType": {
            "type": "string",
            "enum": [
              "REALIZES",
              "EMBODIES",
              "SATISFIES",
              "PRESCRIBES",
              "INTEGRATES",
              "YIELDS",
              "PERFORMS",
              "UTILIZES",
              "CONSUMES",
              "CONSTRAINED_BY",
              "GOVERNED_BY",
              "PROTECTS",
              "GENERATES",
              "INDICATES",
              "MITIGATES",
              "VALIDATES_AGAINST",
              "ORCHESTRATED_BY",
              "SUPPORTED_BY",
              "EMBEDDED_IN",
              "EVOLVES_FROM",
              "SUPERSEDES",
              "EXPANDS",
              "INTEGRATES_INTO",
              "LOCALIZES_FUNCTION",
              "SPECIALIZES_TECHNIQUE",
              "YIELDS_CONSTITUENT",
              "CONSTITUENT_GOVERNED_BY",
              "COMPOSED_BY_CONSTITUENT"
            ],
            "description": "Specific typed relationship."
          },
          "targetNodeId": {
            "type": "string"
          },
          "description": {
            "type": "string"
          }
        },
        "additionalProperties": false
      }
    },
    "metadata": {
      "type": "object",
      "required": ["tags", "confidenceScore", "sourceReference", "createdAt", "auditTrail"],
      "properties": {
        "tags": {
          "type": "array",
          "items": { "type": "string" }
        },
        "categoryAmbiguity": {
          "type": "object",
          "description": "Captures alternative plausible category classifications when the node spans multiple technical layers.",
          "required": ["isAmbiguous", "primaryJustification", "alternativeCategories"],
          "properties": {
            "isAmbiguous": { "type": "boolean" },
            "primaryJustification": { "type": "string" },
            "alternativeCategories": {
              "type": "array",
              "items": {
                "type": "object",
                "required": ["category", "justification", "confidence"],
                "properties": {
                  "category": {
                    "type": "string",
                    "enum": [
                      "Reality", "ActionInterfaceAndActuation", "ConcreteTechnicalArtifact",
                      "TechnicalBlueprint", "TechnicalAgent", "TechnicalProcess",
                      "TechnicalStandard", "TechnicalConstraint", "TechnicalInfrastructure",
                      "TechnicalFeedback", "TechnicalAct", "TechnicalPrinciple",
                      "TechnicalStrategy", "TechnicalFramework", "TechnicalOperator",
                      "ProductionTechnicalObject", "ConstitutiveTechnicalObject", "Technique",
                      "OperativeTechnique", "ConstitutiveTechnique", "TechnicalPurpose",
                      "TechnicalFunction", "TechnicalArchitecture", "TechnicalSpecification",
                      "TechnicalEvolution", "TechnicalLabor", "TechnicalInstitution",
                      "TechnicalResearch", "TechnicalCompetence", "TechnicalFailure",
                      "TechnicalRequirement", "Verification", "Maintenance", "Security",
                      "Resource", "TechnicalObsolescence"
                    ]
                  },
                  "justification": { "type": "string" },
                  "confidence": { "type": "number", "minimum": 0, "maximum": 1 }
                },
                "additionalProperties": false
              }
            }
          },
          "additionalProperties": false
        },
        "confidenceScore": {
          "type": "number",
          "minimum": 0,
          "maximum": 1
        },
        "sourceReference": { "type": "string" },
        "createdAt": { "type": "string", "format": "date-time" },
        "auditTrail": {
          "type": "array",
          "items": {
            "type": "object",
            "required": ["reviewDate", "reviewNote"],
            "properties": {
              "reviewDate": { "type": "string", "format": "date" },
              "reviewNote": { "type": "string" }
            },
            "additionalProperties": false
          }
        }
      },
      "additionalProperties": false
    }
  },
  "allOf": [
    { "if": { "properties": { "category": { "const": "Reality" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/RealitySpecific" } } } },
    { "if": { "properties": { "category": { "const": "ActionInterfaceAndActuation" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/ActionInterfaceAndActuationSpecific" } } } },
    { "if": { "properties": { "category": { "const": "ConcreteTechnicalArtifact" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/ConcreteTechnicalArtifactSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalBlueprint" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalBlueprintSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalAgent" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalAgentSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalProcess" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalProcessSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalStandard" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalStandardSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalConstraint" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalConstraintSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalInfrastructure" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalInfrastructureSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalFeedback" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalFeedbackSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalAct" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalActSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalPrinciple" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalPrincipleSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalStrategy" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalStrategySpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalFramework" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalFrameworkSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalOperator" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalOperatorSpecific" } } } },
    { "if": { "properties": { "category": { "const": "ProductionTechnicalObject" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/ProductionTechnicalObjectSpecific" } } } },
    { "if": { "properties": { "category": { "const": "ConstitutiveTechnicalObject" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/ConstitutiveTechnicalObjectSpecific" } } } },
    { "if": { "properties": { "category": { "const": "Technique" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechniqueSpecific" } } } },
    { "if": { "properties": { "category": { "const": "OperativeTechnique" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/OperativeTechniqueSpecific" } } } },
    { "if": { "properties": { "category": { "const": "ConstitutiveTechnique" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/ConstitutiveTechniqueSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalPurpose" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalPurposeSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalFunction" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalFunctionSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalArchitecture" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalArchitectureSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalSpecification" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalSpecificationSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalEvolution" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalEvolutionSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalLabor" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalLaborSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalInstitution" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalInstitutionSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalResearch" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalResearchSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalCompetence" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalCompetenceSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalFailure" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalFailureSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalRequirement" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalRequirementSpecific" } } } },
    { "if": { "properties": { "category": { "const": "Verification" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/VerificationSpecific" } } } },
    { "if": { "properties": { "category": { "const": "Maintenance" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/MaintenanceSpecific" } } } },
    { "if": { "properties": { "category": { "const": "Security" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/SecuritySpecific" } } } },
    { "if": { "properties": { "category": { "const": "Resource" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/ResourceSpecific" } } } },
    { "if": { "properties": { "category": { "const": "TechnicalObsolescence" } } }, "then": { "properties": { "specific": { "$ref": "#/$defs/TechnicalObsolescenceSpecific" } } } }
  ],
  "$defs": {
    "RealitySpecific": {
      "type": "object",
      "required": ["ontologicalClass", "observability", "temporalProfile", "levelOfExistence", "conceptEvaluationNote"],
      "properties": {
        "ontologicalClass": {
          "type": "string",
          "enum": ["Ontic.Existential.Substantive", "Ontic.Existential.Processual", "Ontic.Existential.Entity", "Ontic.Existential.Mechanism", "Ontic.Dynamical.Event", "Ontic.Dynamical.Process", "Ontic.Dynamical.Stochastic", "Ontic.Dynamical.EventStream", "Ontic.Dynamical.MixtureEventStream", "Ontic.Dynamical.Phenomena", "Ontic.Dynamical.Epiphenomena", "Ontic.Agency.Agent", "Synontic.Property", "Synontic.Aspect", "Synontic.StateModel", "Synontic.VariableAspect"],
          "description": "Primary ontological class from controlled vocabulary."
        },
        "observability": { "type": "string", "enum": ["observable", "latent", "partiallyObservable"] },
        "temporalProfile": { "type": "string", "enum": ["endurant", "perdurant", "transient"] },
        "levelOfExistence": { "type": "string", "enum": ["zero-order", "first-order", "second-order", "third-order"] },
        "conceptEvaluationNote": { "type": "string" }
      },
      "additionalProperties": false
    },
    "ActionInterfaceAndActuationSpecific": {
      "type": "object",
      "required": ["transductionMethod", "actuationMechanism", "encodingFormat"],
      "properties": {
        "transductionMethod": { "type": "string", "description": "How energy/information is converted into action." },
        "actuationMechanism": { "type": "string", "description": "Physical or logical effector (e.g., robotic gripper, CNC spindle)." },
        "encodingFormat": { "type": "string", "description": "Syntax or protocol for intent encoding (e.g., G-code, API call)." }
      },
      "additionalProperties": false
    },
    "ConcreteTechnicalArtifactSpecific": {
      "type": "object",
      "required": ["materialComposition", "dimensions", "interfaceSpec", "functionalState"],
      "properties": {
        "materialComposition": { "type": "string" },
        "dimensions": { "type": "string" },
        "interfaceSpec": { "type": "string" },
        "functionalState": { "type": "string", "enum": ["operational", "malfunctional", "degraded", "inoperative"] }
      },
      "additionalProperties": false
    },
    "TechnicalBlueprintSpecific": {
      "type": "object",
      "required": ["representationFormat", "formalism", "generativeRules"],
      "properties": {
        "representationFormat": { "type": "string", "description": "CAD, source code, PCB Gerber, BOM, etc." },
        "formalism": { "type": "string", "description": "Underlying language or schema." },
        "generativeRules": { "type": "array", "items": { "type": "string" }, "description": "Constraints that guide instantiation." }
      },
      "additionalProperties": false
    },
    "TechnicalAgentSpecific": {
      "type": "object",
      "required": ["agentType", "capabilities", "autonomyLevel", "goalStructure"],
      "properties": {
        "agentType": { "type": "string", "enum": ["human", "machine", "hybridSystem", "institution"] },
        "capabilities": { "type": "array", "items": { "type": "string" } },
        "autonomyLevel": { "type": "string" },
        "goalStructure": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalProcessSpecific": {
      "type": "object",
      "required": ["processType", "inputs", "outputs", "validationMethod"],
      "properties": {
        "processType": { "type": "string" },
        "inputs": { "type": "array", "items": { "type": "string" } },
        "outputs": { "type": "array", "items": { "type": "string" } },
        "validationMethod": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalStandardSpecific": {
      "type": "object",
      "required": ["standardType", "complianceCriteria", "measurementBasis"],
      "properties": {
        "standardType": { "type": "string" },
        "complianceCriteria": { "type": "string" },
        "measurementBasis": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalConstraintSpecific": {
      "type": "object",
      "required": ["constraintType", "boundedResource", "failureMode"],
      "properties": {
        "constraintType": { "type": "string" },
        "boundedResource": { "type": "string" },
        "failureMode": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalInfrastructureSpecific": {
      "type": "object",
      "required": ["infrastructureType", "storageMechanism", "communicationMode"],
      "properties": {
        "infrastructureType": { "type": "string" },
        "storageMechanism": { "type": "string" },
        "communicationMode": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalFeedbackSpecific": {
      "type": "object",
      "required": ["feedbackType", "signalSource", "adaptationTarget"],
      "properties": {
        "feedbackType": { "type": "string" },
        "signalSource": { "type": "string" },
        "adaptationTarget": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalActSpecific": {
      "type": "object",
      "required": ["actType", "intent", "target", "outcome"],
      "properties": {
        "actType": { "type": "string" },
        "intent": { "type": "string" },
        "target": { "type": "string" },
        "outcome": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalPrincipleSpecific": {
      "type": "object",
      "required": ["principleType", "formalStatement", "applicability"],
      "properties": {
        "principleType": { "type": "string" },
        "formalStatement": { "type": "string" },
        "applicability": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalStrategySpecific": {
      "type": "object",
      "required": ["strategyType", "optimizationGoal", "decisionHeuristic"],
      "properties": {
        "strategyType": { "type": "string" },
        "optimizationGoal": { "type": "string" },
        "decisionHeuristic": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalFrameworkSpecific": {
      "type": "object",
      "required": ["frameworkType", "coreAssumptions", "integrationScope"],
      "properties": {
        "frameworkType": { "type": "string" },
        "coreAssumptions": { "type": "string" },
        "integrationScope": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalOperatorSpecific": {
      "type": "object",
      "required": ["operatorType", "transformationRule", "operandType"],
      "properties": {
        "operatorType": { "type": "string" },
        "transformationRule": { "type": "string" },
        "operandType": { "type": "string" }
      },
      "additionalProperties": false
    },
    "ProductionTechnicalObjectSpecific": {
      "type": "object",
      "required": ["deploymentContext", "operationalEnvironment", "valueDelivery"],
      "properties": {
        "deploymentContext": { "type": "string" },
        "operationalEnvironment": { "type": "string" },
        "valueDelivery": { "type": "string", "description": "Ultimate purpose or service provided." }
      },
      "additionalProperties": false
    },
    "ConstitutiveTechnicalObjectSpecific": {
      "type": "object",
      "required": ["roleInAssembly", "integrationInterface", "dependencyDepth"],
      "properties": {
        "roleInAssembly": { "type": "string" },
        "integrationInterface": { "type": "string" },
        "dependencyDepth": { "type": "integer", "minimum": 0 }
      },
      "additionalProperties": false
    },
    "TechniqueSpecific": {
      "type": "object",
      "required": ["knowledgeDomain", "codificationLevel", "transmissionMethod"],
      "properties": {
        "knowledgeDomain": { "type": "string" },
        "codificationLevel": { "type": "string", "enum": ["tacit", "explicit", "mixed"] },
        "transmissionMethod": { "type": "string" }
      },
      "additionalProperties": false
    },
    "OperativeTechniqueSpecific": {
      "type": "object",
      "required": ["contextualParameters", "agentSkillLevel", "situatedOutcome"],
      "properties": {
        "contextualParameters": { "type": "string" },
        "agentSkillLevel": { "type": "string" },
        "situatedOutcome": { "type": "string" }
      },
      "additionalProperties": false
    },
    "ConstitutiveTechniqueSpecific": {
      "type": "object",
      "required": ["targetArtifactType", "precisionClass", "qualityAssurance"],
      "properties": {
        "targetArtifactType": { "type": "string" },
        "precisionClass": { "type": "string" },
        "qualityAssurance": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalPurposeSpecific": {
      "type": "object",
      "required": ["teleologicalStatement", "stakeholder", "successCriteria"],
      "properties": {
        "teleologicalStatement": { "type": "string" },
        "stakeholder": { "type": "string" },
        "successCriteria": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalFunctionSpecific": {
      "type": "object",
      "required": ["inputOutputMapping", "physicalLaw", "abstractionLevel"],
      "properties": {
        "inputOutputMapping": { "type": "string" },
        "physicalLaw": { "type": "string" },
        "abstractionLevel": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalArchitectureSpecific": {
      "type": "object",
      "required": ["topology", "decompositionStyle", "interfaceProtocol"],
      "properties": {
        "topology": { "type": "string" },
        "decompositionStyle": { "type": "string" },
        "interfaceProtocol": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalSpecificationSpecific": {
      "type": "object",
      "required": ["metric", "valueRange", "testMethod"],
      "properties": {
        "metric": { "type": "string" },
        "valueRange": { "type": "string" },
        "testMethod": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalEvolutionSpecific": {
      "type": "object",
      "required": ["generation", "drivingForces", "keyInnovations"],
      "properties": {
        "generation": { "type": "string" },
        "drivingForces": { "type": "array", "items": { "type": "string" } },
        "keyInnovations": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    },
    "TechnicalLaborSpecific": {
      "type": "object",
      "required": ["laborType", "skillIntensity", "compensationModel"],
      "properties": {
        "laborType": { "type": "string" },
        "skillIntensity": { "type": "string" },
        "compensationModel": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalInstitutionSpecific": {
      "type": "object",
      "required": ["institutionType", "governanceStructure", "standardizationRole"],
      "properties": {
        "institutionType": { "type": "string" },
        "governanceStructure": { "type": "string" },
        "standardizationRole": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalResearchSpecific": {
      "type": "object",
      "required": ["researchMethod", "knowledgeOutput", "technologyReadinessLevel"],
      "properties": {
        "researchMethod": { "type": "string" },
        "knowledgeOutput": { "type": "string" },
        "technologyReadinessLevel": { "type": "integer", "minimum": 1, "maximum": 9 }
      },
      "additionalProperties": false
    },
    "TechnicalCompetenceSpecific": {
      "type": "object",
      "required": ["competenceArea", "proficiencyLevel", "assessmentMethod"],
      "properties": {
        "competenceArea": { "type": "string" },
        "proficiencyLevel": { "type": "string" },
        "assessmentMethod": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalFailureSpecific": {
      "type": "object",
      "required": ["failureMode", "rootCause", "severityClass"],
      "properties": {
        "failureMode": { "type": "string" },
        "rootCause": { "type": "string" },
        "severityClass": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalRequirementSpecific": {
      "type": "object",
      "required": ["requirementType", "priority", "verificationMethod"],
      "properties": {
        "requirementType": { "type": "string" },
        "priority": { "type": "string" },
        "verificationMethod": { "type": "string" }
      },
      "additionalProperties": false
    },
    "VerificationSpecific": {
      "type": "object",
      "required": ["verificationType", "testProcedure", "acceptanceCriteria"],
      "properties": {
        "verificationType": { "type": "string" },
        "testProcedure": { "type": "string" },
        "acceptanceCriteria": { "type": "string" }
      },
      "additionalProperties": false
    },
    "MaintenanceSpecific": {
      "type": "object",
      "required": ["maintenanceType", "schedule", "interventionActions"],
      "properties": {
        "maintenanceType": { "type": "string", "enum": ["preventive", "corrective", "predictive"] },
        "schedule": { "type": "string" },
        "interventionActions": { "type": "array", "items": { "type": "string" } }
      },
      "additionalProperties": false
    },
    "SecuritySpecific": {
      "type": "object",
      "required": ["securityAttribute", "threatModel", "controlMechanism"],
      "properties": {
        "securityAttribute": { "type": "string", "enum": ["confidentiality", "integrity", "availability", "authenticity"] },
        "threatModel": { "type": "string" },
        "controlMechanism": { "type": "string" }
      },
      "additionalProperties": false
    },
    "ResourceSpecific": {
      "type": "object",
      "required": ["resourceType", "measurableUnit", "consumptionProfile"],
      "properties": {
        "resourceType": { "type": "string" },
        "measurableUnit": { "type": "string" },
        "consumptionProfile": { "type": "string" }
      },
      "additionalProperties": false
    },
    "TechnicalObsolescenceSpecific": {
      "type": "object",
      "required": ["obsolescenceType", "triggerEvent", "replacementArtifact"],
      "properties": {
        "obsolescenceType": { "type": "string", "enum": ["technological", "economic", "social"] },
        "triggerEvent": { "type": "string" },
        "replacementArtifact": { "type": "string" }
      },
      "additionalProperties": false
    }
  },
  "additionalProperties": false
}
```

subject to

# Philosophia Artium Technicarum et Operis

> In this note, we will analyze the concept of purposeful (agentic) operation and its primary driver: technique - that is capturing technical practice.

> Technical practice can be characterized as the structured process by which an agent transforms, constructs, operates, and maintains material or informational artifacts to bring about desired states in the world.

> This note seeks to systematize a philosophy of technique and operation that can serve as a conceptual foundation for organizing the ideas used to explain operation and praxis across diverse fields and tasks.

## Formulation

> Which are the sets of concept that characterize  epistemic practice? How to capture all of this concept in a database?

| **Category** | **Description** | **Instance(s)** |
| --- | --- | --- |
| **Reality** | The ontological substrate comprising the actual physical, chemical, biological, informational, and social structures that both constrain and respond to technical intervention. Reality is the medium of action: it offers affordances, resists actuation, degrades artifacts, and ultimately validates or negates technical outcomes. | Steel beam, fluid flow, electric grid, living tissue, user population, electromagnetic spectrum, geological formation, supply chain, software runtime environment, urban infrastructure. |
| **Action Interface & Actuation** | The motoric and encoding boundary through which an agent imparts energy, information, or structure onto reality. Includes effector hardware, actuation transducers, formative tools, and the encoding of intent into executable commands. | CNC spindle + G‑code; robotic gripper + motion controller; keyboard + IDE + compilation pipeline; human hand + chisel; relay + SCADA signal. |
| **Concrete Technical Artifact (Technical Object)** | A specific, fully‑specified object, system, or code module that has been produced or is being operated; the primary carrier of technical effect. **Zero free parameters** – every dimension, material, logic branch, and interface is fixed. Can be evaluated as functional/malfunctional, safe/unsafe, efficient/inefficient. | A particular bridge (with coordinates), a compiled binary `app.exe`, a fully‑configured Kubernetes cluster, a printed turbine blade, a patient‑specific surgical implant, installation‑ready circuit board. |
| **Technical Blueprint** | The generative description that prescribes how to create, assemble, or configure an artifact. A formalized recipe that abstracts over material instances. | Engineering drawing, architect’s plan, source code listing, PCB Gerber files, Bill of Materials + assembly instructions, molecular synthesis route, infrastructure‑as‑code template. |
| **Technical Agent** | Entity that executes technical operations by utilizing tools, energy, and instructions. | Engineer, artisan, construction crew, surgical robot, industrial control system, compiler, build pipeline, autonomous drone, automated fabrication system. |
| **Technical Process (Activity)** | Ordered, temporally‑extended sequence of technical acts that transform inputs (materials, energy, information) into outputs (artifacts, services, changed states). Defines the dynamics of making, maintaining, and operating. | Assembly line sequence, software development lifecycle, continuous integration pipeline, construction project schedule, sterilization protocol, dynamic power‑up sequence. |
| **Technical Standard** | Normative specification that governs form, fit, function, safety, interoperability, or performance of an artifact or process. | ISO dimension tolerance, UL safety code, API specification, HTTP protocol, electrical code, medical device sterility assurance level, coding style guide, materials grade. |
| **Technical Constraint** | Any bound on achievable action imposed by physical law, material properties, resource availability, or social regulation. | Tensile strength limit, noise floor, power budget, time deadline, regulatory ban, scarce rare‑earth element, network latency floor, computational complexity, thermal hotspot, toxicity threshold, human ergonomic limit. |
| **Technical Infrastructure** | The ambient capital—material, energetic, informational, institutional—that makes sustained technical practice possible. | Power grid, water supply, internet backbone, factory floor, tool chain, version control repository, laboratory bench, standards body, certification authority, supply chain. |
| **Technical Feedback** | Signal that indicates the real‑world effect of a technical act, enabling adjustment, optimization, and error correction. | Stress‑strain gauge reading, build log error message, user complaint, wear debris in lubricant, temperature rise, latency spike, crash report, A/B test result, pass/fail quality inspection. |
| **Technical Act** | Primitive, non‑decomposable operation that a technical agent performs on reality (or on an artifact). | Cutting, welding, bolting, writing a line of code, compiling, deploying, measuring torque, pressing a button, casting a vote in a control system, issuing an API call, flipping a switch. |
| **Technical Principle** | Foundational design law, operating axiom, or reliability rule that governs how technical agents should structure interventions and artifacts to ensure safety, efficiency, robustness, and functionality. | Least privilege, defense in depth, fail‑safe, idempotency, separation of concerns, KISS, YAGNI, tolerance for use, design for manufacturability, loose coupling, energy‑minimization, ergonomic adjustability, redundancy, graceful degradation. |
| **Technical Strategy** | Context‑sensitive, resource‑aware regime of planning and decision‑making that organizes the sequence, decomposition, and prioritization of technical work under real‑world constraints. | Waterfall, Agile, spiral, prototyping‑first, concurrent engineering, design‑build‑test‑iterate, modular incremental deployment, brownfield vs greenfield, security‑by‑design, lean production, just‑in‑time, preventive maintenance scheduling, blue‑green deployment. |
| **Technical Framework** | The overarching problem‑structuring and solution‑generation logic within which technical agents interpret requirements, decompose complexity, and synthesize artifacts. | Systems engineering, design thinking, TRIZ, axiomatic design, root cause analysis, failure modes and effects analysis (FMEA), control theory, operations research, generative design, cyber‑physical systems, mechatronics. |
| **Technical Operator** | Formal, procedural, or physical mechanism used to transform, assemble, verify, or maintain technical artifacts. Operators are the “verbs” of technical practice. | Milling (subtractive), injection moulding (formative), soldering (joining), refactoring (code transformation), integration testing, heat‑treating, etching, calibration, patching, container orchestration, concrete pouring. |
| **Production Technical Object** | The final, deployable artifact that fulfills the ultimate technical purpose in its operational environment. It is the end-product of the technical process, ready to deliver value, effect, or service to a user or broader system. | A completed consumer smartphone, a commissioned nuclear reactor, a deployed SaaS platform, a delivered commercial aircraft, a released video game, an operational MRI machine. |
| **Constitutive Technical Object** | An intermediate artifact, component, or sub-assembly that serves as a building block within a larger Production Technical Object. It possesses localized functions but derives its ultimate purpose from integration into the whole. | A lithium-ion battery cell, a microcontroller chip, a custom UI widget library, a milled chassis frame, a ball bearing, a normalized SQL database schema, a precast concrete pillar. |
| **Technique** | The generalized, culturally or professionally transmitted body of knowledge regarding how to achieve a specific type of technical effect. A codified or tacit "way of doing" that transcends a singular execution. | Arc welding, precision machining, chromatography, forging, test-driven development, microservices design, cognitive walkthrough, statistical process control. |
| **Operative Technique** | The context-specific, situated application of a generalized Technique by a Technical Agent to transform a specific material or informational state. The technique as actively performed in situ. | A welder executing a specific TIG pass on an aluminum pipe; a developer applying test-driven development to write an authentication module; a machinist setting specific feed rates for titanium. |
| **Constitutive Technique** | The specialized methods, processes, and know-how dedicated specifically to the creation, testing, and integration of Constitutive Technical Objects. The "making of the parts." | Photolithography for semiconductors, die-casting for engine blocks, unit testing for software modules, powder metallurgy for gears, spectral analysis for raw material verification. |
| **Technical Purpose** | The teleological orientation of an artifact or process; the intended ultimate impact on reality, human experience, or a broader system. The "why" of the technical endeavor, distinct from its mechanistic function. | Transporting passengers across the Atlantic; curing a bacterial infection; providing real-time financial data to traders; generating zero-carbon electricity; reducing cognitive load for air traffic controllers. |
| **Technical Function** | The objective, mechanistic input-output relationship of an artifact or system, abstracted from its ultimate purpose. What a system *does* physically or logically to transform states. | Converting chemical energy to rotational kinetic energy; filtering particles larger than 5 microns; translating HTTP requests into SQL queries; amplifying voltage by a factor of 10; algorithmically smoothing signal noise. |
| **Technical Architecture** | The fundamental structural organization of a system, embodied in its components, their relationships to each other and the environment, and the principles governing its design and evolution. | Client-server model, microservices topology, monocoque chassis design, layered network model (OSI), microkernel OS design, grid-tied solar array topology, hub-and-spoke logistics network. |
| **Technical Specification** | A precise, quantitative, and unambiguous statement of the technical requirements, performance parameters, and interface conditions an artifact must satisfy. The contractual boundary between design and verification. | "API response time < 200ms at p99"; "Operational temperature range: -40°C to +85°C"; "Maximum axle load: 20 tons"; "Supports 10,000 concurrent WebSocket connections"; "Battery capacity retention > 80% after 1000 cycles." |
| **Technical Evolution** | The cumulative, historical trajectory of change in technical artifacts, processes, or knowledge over time, driven by iterative problem-solving, standardization, market selection, and shifting constraints. | The transition from vacuum tubes to transistors to integrated circuits; the shift from water power to steam to electric motors; the progression from monolithic to serverless software design; the evolution of bicycle drivetrain mechanisms. |
| **Technical Labor** | The purposive expenditure of human cognitive and physical effort applied to technical processes. The embodied execution of technique by human agents within a socio-economic framework. | A sysadmin diagnosing a network outage at 3 AM; an electrician pulling wire through conduit; a programmer refactoring a legacy codebase; a technician calibrating sensors on a factory floor. |
| **Technical Institution** | The formalized, durable social structures—organizations, regulatory bodies, or professional communities—that organize, govern, incentivize, and sustain technical practice and knowledge transmission. | IEEE, ASME, FDA, FAA, a corporate R&D division, a university engineering department, a professional licensing board, an open-source software foundation (e.g., Linux Foundation). |
| **Technical Research** | Systematic, methodological investigation aimed at discovering new technical principles, materials, processes, or capabilities, expanding the boundary of the technically possible. | Developing solid-state battery chemistry; testing a novel aerodynamic hull shape in a wind tunnel; training a new large language model architecture; synthesizing a new polymer blend; exploring quantum error correction algorithms. |
| **Technical Competence** | The embodied, acquired capacity of a Technical Agent to reliably execute Technical Processes and Operative Techniques, yielding successful outcomes within accepted tolerances. | A senior surgeon’s ability to perform a laparoscopic procedure; a master machinist’s intuitive feel for cutting speeds; a principal engineer’s aptitude for system design; a pilot’s muscle memory for emergency procedures. |
| **Technical Failure** | The state or event wherein an artifact or process deviates from its Technical Specification or required Technical Function under specified operating conditions, potentially leading to loss of purpose, safety hazards, or systemic degradation. | Stack overflow crash in production; fatigue-induced fracture of an aircraft fuselage; thermal runaway in a lithium battery; failure of a SCADA system to close a valve; bridge collapse under load; authentication bypass vulnerability. |
| **Technical Requirement** | Formalized desired state, need, or performance objective that initiates technical practice | "The vehicle shall achieve 0-60 mph in under 5 seconds"; "The system must support 99.99% uptime"; "The device shall not exceed 50 decibels at 1 meter under load"; "User passwords must be salted and hashed.” |
| **Verification** | The systematic process of evaluating an artifact, process, or service to determine whether it accurately fulfills its Technical Specification or Blueprint. It answers the question of "Are we building the system right?" through objective evidence. | Code linting/static analysis, physical dimension inspection with calipers, unit testing, circuit continuity checking, code review against a style guide, automated regression testing, model checking against formal properties. |
| **Maintenance** | The ordered set of technical acts and processes performed on an operational artifact to retain it in, or restore it to, a state in which it can reliably perform its Technical Function. It counteracts the entropic degradation imposed by Reality. | Replacing worn brake pads, applying a security patch to an OS, lubricating a bearing, clearing a blocked pipe, defragmenting a hard drive, recalibrating a sensor array, scraping and repainting a steel hull. |
| **Security** | The domain of technical principles, constraints, and processes concerned with protecting an artifact or system from unauthorized access, use, disclosure, disruption, modification, or destruction. It manages adversarial constraints within the operational environment. | Role-based access control (RBAC), AES-256 encryption at rest, network firewall rule sets, code obfuscation, physical perimeter fencing, multi-factor authentication (MFA), input sanitization against SQLi, hardware security modules (HSMs). |
| **Resource** | The consumable or non-consumable inputs—matter, energy, information, time, or capital—that are required, transformed, or consumed by a Technical Agent or Process to produce, operate, or maintain an artifact. | Gallium arsenide substrate, megawatt-hours of electricity, API rate limits, engineer labor-hours, venture capital funding, silicon wafers, gigabytes of RAM, clean water for industrial cooling, developer seat licenses. |
| **Technical Obsolescence** | The state wherein an artifact is no longer technically viable, economically justifiable, or socially supported compared to available alternatives, regardless of its current functional state. | The state wherein an artifact is no longer technically viable, economically justifiable, or socially supported compared to available alternatives, regardless of its current functional state. |
