Student Name: JBanks222
Date: April 15, 2026

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Before adding the missing tests, the application only had partial coverage and many important behaviors were not being checked. After completing the unit and API tests, the verified coverage increased from 53% to 98%. The final test suite contains 23 passing tests. This is a major improvement because the most important parts of the application, including creating fruits, updating them, deleting them, searching inventory, and validating model data, are now covered by automated tests.

## Untested Code: Effects

It was harder to understand the full behavior of the application when only a few tests were available. I could read the routes and models, but without tests it was not always obvious what edge cases had already been considered or what kinds of input were expected to fail. Manual API testing helped me learn the endpoints, but it also took longer and felt less reliable because it depended on repeating the same requests by hand.

Having few tests made the codebase feel more fragile. If I changed one part of the application, there was less confidence that another part would still work correctly. The lack of coverage also meant that some important user paths, especially search and update behavior, could easily break without being noticed right away.

## Adding Tests

I added tests by reviewing the model methods and the Flask routes one by one. I identified missing coverage in quantity validation, average quantity calculations, common fruit counting, search filters, and REST endpoints. Then I wrote focused tests to confirm both successful behavior and error handling.

A unit test checks one small piece of logic in isolation, such as a model method or validator. An API test checks how the application behaves from the user’s perspective by sending HTTP requests and validating the response. Both are valuable because unit tests catch logic issues quickly, while API tests confirm that the full request and response flow works correctly.

## Automation

Automating the tests with pytest and coverage made the project much easier to evaluate. Instead of guessing whether the application was stable, I could run one command and immediately see whether all tests passed and which code paths were still untested. This saves time, improves consistency, and supports continuous integration practices.

## New Features

Working on tested baseline code gave me more confidence when thinking about future features. Once the current functionality is protected by tests, it becomes much safer to add analytics or expiration tracking without worrying that basic inventory operations will accidentally break.

## Future

This experience showed me that testing is not just a school requirement, but a core part of professional software development. Going forward, I want to write tests earlier in the development process so that new code is easier to maintain, safer to refactor, and more dependable for users.
