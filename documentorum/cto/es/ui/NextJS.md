# NextJS


## Routes

Next.js uses a file-based routing system to automatically discover and generate routes for your application. This routing system is based on the structure of the `pages` directory in your Next.js project. Here’s how Next.js discovers routes:

1. **File Structure**: Next.js looks for JavaScript (`.js` or `.jsx`) files inside the `pages` directory of your project. Each file in this directory represents a route in your application.
    
    For example:
    
    ```
    pages/
    ├── index.js         // Represents the root route "/"
    ├── about.js         // Represents the "/about" route
    ├── products/
    │   ├── index.js     // Represents the "/products" route
    │   ├── item.js      // Represents the "/products/item" route
    │   └── category.js  // Represents the "/products/category" route
    ├── contact.js       // Represents the "/contact" route
    └── [...].js         // Represents catch-all routes
    ```
    
2. **Dynamic Routes**: You can use square brackets `[]` in file names to create dynamic routes. For example, `pages/posts/[id].js` would match URLs like `/posts/1`, `/posts/2`, and so on.
3. **Catch-All Routes**: You can use an ellipsis `...` in square brackets `[...]` to create catch-all routes. For example, `pages/users/[...slug].js` would match URLs like `/users/john`, `/users/john/posts`, and so on.
4. **Nested Routes**: You can organize your pages into subdirectories within the `pages` directory to create nested routes, as shown in the example above with the `products` directory.
5. **Default Export**: Each file in the `pages` directory should have a default export that represents the content for that route. This export should be a React component.
6. **Index Routes**: If a file named `index.js` is present in a subdirectory of `pages`, it represents the default route for that subdirectory. For example, `pages/products/index.js` represents the `/products` route.
7. **Special Routes**: There are some special file names that have reserved meanings, such as `_app.js`, `_document.js`, and `_error.js`. These files are used for customizing the overall app layout, document structure, and error handling, respectively.
8. **API Routes**: Files inside the `pages/api` directory represent serverless API routes. These files don’t create client-side routes but serve as server-side endpoints.

Next.js uses this file-based routing system to automatically generate routes for your application during the build process. It creates a route for each JavaScript file in the `pages` directory, and you can navigate to these routes in your application without the need for additional configuration. This simplicity and convention-over-configuration approach make it easy to get started with routing in Next.js.

## References

- https://news.ycombinator.com/item?id=41866583
