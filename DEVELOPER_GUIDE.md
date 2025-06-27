# Developer Guide

This guide provides instructions for developers working on the Book Review Service project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up the Development Environment](#setting-up-the-development-environment)
- [Running Tests](#running-tests)
- [Contributing](#contributing)
- [Branching and Pull Request Process](#branching-and-pull-request-process)

## Prerequisites

Before you begin, ensure you have the following installed:

* Python 3.7+
* Git
* A virtual environment tool (e.g., `venv` or `conda`)

## Setting Up the Development Environment

1. **Clone the repository:**
```
bash
   git clone <repository_url>
   cd <project_directory>
   
```
2. **Create and activate a virtual environment:**

   Using `venv`:
```
bash
   python -m venv .venv
   source .venv/bin/activate
   
```
Using `conda`:
```
bash
   conda create -n book-review-service python=3.8
   conda activate book-review-service
   
```
3. **Install dependencies:**
```
bash
   pip install -r requirements.txt
   
```
4. **Set up the database:**

   Follow the instructions in the `migrations` directory to set up and migrate the database.

## Running Tests

To run the tests, use the following command:
```
bash
pytest
```
You can also run specific test files or tests using pytest options. Refer to the pytest documentation for more details.

## Contributing

We welcome contributions to the Book Review Service project! To contribute, please follow these steps:

1. **Fork the repository.**
2. **Create a feature branch** for your work.
3. **Make your changes** and ensure they adhere to the project's coding standards.
4. **Write and run tests** to cover your changes.
5. **Commit your changes** with clear and concise commit messages.
6. **Push your branch** to your fork.
7. **Create a Pull Request (PR)** to the `main` branch of the main repository.

## Branching and Pull Request Process

The project uses a **feature branching model**.

* **Feature Branches:** For every new feature or bug fix, create a dedicated branch off of `main`. Name your branch descriptively (e.g., `feat/add-user-authentication`, `fix/database-connection-issue`).
* **Development:** Develop your feature or fix entirely within this feature branch.
* **Pull Requests:** Once your work is complete and tested, create a Pull Request from your feature branch to the `main` branch.
* **Review and Merge:** Your PR will be reviewed by maintainers. Upon approval, your branch will be merged into `main`.

This process helps keep the `main` branch stable and ensures that all changes are reviewed before being integrated.