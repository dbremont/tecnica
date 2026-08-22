# Swagger

> Swagger is an open-source framework for designing, documenting, and testing RESTful APIs, simplifying API development and enabling interactive API exploration.
> 

## Swagger Annotations

1. **[SwaggerOperation]**
    - Used to describe an API operation or endpoint.
    - Allows specifying the operation’s HTTP method, path, and summary.
2. **[ProducesResponseType]**
    - Used to specify the possible HTTP response types and status codes for an operation.
3. **[SwaggerResponse]**
    - Used to document a single HTTP response for an operation, including its status code and description.
4. **[SwaggerRequestExample]**
    - Allows defining examples of request payloads for an operation.
5. **[SwaggerResponseExample]**
    - Allows defining examples of response payloads for an operation.
6. **[SwaggerRequestBody]**
    - Used to describe the request body of an operation.
7. **[SwaggerResponseHeader]**
    - Specifies a response header in the Swagger documentation.
8. **[SwaggerOperationFilter]**
    - Allows customizing the operation’s Swagger documentation at runtime.
9. **[SwaggerSchemaFilter]**
    - Used for customizing the schema of a model in Swagger documentation.
10. **[SwaggerTag]**
    - Specifies tags for organizing and categorizing operations.
11. **[SwaggerSecurityRequirement]**
    - Defines security requirements for an operation.
12. **[SwaggerSecurity]**
    - Used to describe security schemes and requirements for an API.
13. **[SwaggerIgnore]**
    - Excludes an operation or property from being documented in Swagger.
14. **[FromQuery]**
    - Used to specify that a parameter should be bound from the query string in HTTP requests.
15. **[FromRoute]**
    - Specifies that a parameter should be bound from the route in HTTP requests.
16. **[FromHeader]**
    - Binds a parameter from an HTTP header.
17. **[FromForm]**
    - Specifies that a parameter should be bound from the form data in a POST request.
18. **[FromRoute]**
    - Specifies that a parameter should be bound from the route in HTTP requests.
19. **[FromRoute]**
    - Specifies that a parameter should be bound from the route in HTTP requests.
20. **[ApiVersion]**
    - Specifies the API version for a controller or action.

## swagger-config.yaml

`swagger-config.yaml`

Swagger UI provides several configuration options that allow you to customize its behavior and appearance when documenting your APIs. Here’s a list of some common Swagger UI options and their descriptions:

1. **url**:
    - Specifies the URL to the Swagger/OpenAPI definition file (JSON or YAML) that Swagger UI should use for documentation.
2. **urls**:
    - Allows you to provide multiple URL definitions, enabling you to switch between different API versions or services in the same Swagger UI instance.
3. **oauth**:
    - Enables OAuth 2.0 authorization support in Swagger UI, allowing users to authenticate and access secured API endpoints.
4. **validatorUrl**:
    - Specifies the URL of an external Swagger validator service. This is used to validate the Swagger/OpenAPI definition against a schema.
5. **docExpansion**:
    - Controls the initial state of the documentation sections. Options include “list,” “full,” “none,” or “fullOnStartup.”
6. **defaultModelRendering**:
    - Defines how models are initially displayed. Options include “model,” “schema,” or “example.”
7. **displayRequestDuration**:
    - Specifies whether to display the request duration (response time) for each API request.
8. **filter**:
    - Allows you to apply a filter to the API operations to display only a subset of endpoints.
9. **operationsSorter**:
    - Controls the sorting of API operations in the UI. Options include “alpha,” “method,” or a custom function.
10. **tagsSorter**:
    - Defines the sorting of tags in the UI. Options include “alpha” or a custom function.
11. **deepLinking**:
    - Enables deep linking to specific sections of the documentation, which updates the URL as you navigate through the documentation.
12. **showExtensions**:
    - Displays vendor extension fields (fields not part of the official OpenAPI specification) in the UI.
13. **displayOperationId**:
    - Specifies whether to display the operation ID next to each operation in the UI.
14. **defaultModelExpandDepth** and **defaultModelsExpandDepth**:
    - Set the default depth for models and model schemas that are expanded by default.
15. **tryItOutEnabled**:
    - Controls whether the “Try it out” functionality is enabled for making API requests directly from the UI.
16. **showCommonExtensions**:
    - Displays common extensions (fields defined by Swagger/OpenAPI extensions) in the UI.
17. **useRequestInterceptor** and **useResponseInterceptor**:
    - Allows you to specify custom JavaScript functions to intercept and modify API requests and responses.
18. **configUrl**:
    - Specifies a URL to an external configuration file to customize Swagger UI settings.
19. **layout**:
    - Specifies the layout of the UI. Options include “BaseLayout,” “StandaloneLayout,” or a custom layout class.
20. **onComplete**:
    - A JavaScript callback function that is executed when Swagger UI has finished loading.

These options can be set when configuring Swagger UI in your ASP.NET Core or Node.js application. Depending on your use case and requirements, you can customize Swagger UI to suit your needs by configuring these options accordingly.

## References

- [Swagger](https://swagger.io/)
- [Swagger Docs](https://medium.com/@niteshsinghal85/enhance-swagger-documentation-with-annotations-in-asp-net-core-d2981803e299)
- [Enhance Swagger Documentation with Annotations in ASP.NET core](https://medium.com/@niteshsinghal85/enhance-swagger-documentation-with-annotations-in-asp-net-core-d2981803e299)
- [Documenting Additional API endpoints in Swagger in ASP.Net Core](https://medium.com/@niteshsinghal85/documenting-additional-api-endpoints-in-swagger-in-asp-net-core-59da9c84e4ba)