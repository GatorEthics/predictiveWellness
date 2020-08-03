# Continuous Integration with GitHub Actions

## The Basics

### The .github Directory

* Each repository should have a `.github` directory
* Every `.github` directory should contain two new sub-directories which are **name-specific**:
  * `ISSUE_TEMPLATE`
  * `workflows`
* Each subdirectory should contain certain files which are also **name-specific**
  * In the `ISSUE_TEMPLATE` directory are files for that give a template for both reporting bugs and requesting features through the GitHub Issue Tracker. These files can contain a customized template, but must have these names:
    * `bug_report.md`
    * `feature_request.md`
  * The `workflows` directory contains the necessary files for continuous integration with GitHub Actions. This file can have any name but requires a `.yml` extension.
* In the `github` directory a **name-specific** file that specifies the pull request template is also required. It should be named: `pull_request_template.md`

#### File Layout Visual:

predictiveWellness
├─ .github
│  ├─ ISSUE_TEMPLATE
│  │  ├─ bug_report.md
│  │  └─ feature_request.md
│  ├─ pull_request_template.md
│  └─ workflows
│     └─ main.yml

**Please ensure that every file in your `.github` directory has the specified name, as GitHub searches for them when implementing templates for issues and PRs, and also running continuous integration checks with GitHub Actions.**

### Other File Requirements

* There are also requirements for files in the root of your repository, which are also **name-specific** including:
  * `.gitignore`: Specifies the files that Git should ignore
  * `.gitmessage`: Provides guidelines for commit messages, and gives a message to a developer after they make a commit to your project
  * `CODE_OF_CONDUCT.md`: A customized code of conduct for developers to define community standards
  * `CONTRIBUTING.md`: A customized list of guidelines for individuals who would like to contribute to your project
  * `LICENSE.md`: Guidelines for sharing software
  * `README.md`: Introduces and explains your project
* These files should not exist in a separate directory but the *root* of your github repository.

#### File Layout Visual:

PredictiveWellness
├─ .gitignore
├─ .gitmessage
├─ CODE_OF_CONDUCT.md
├─ CONTRIBUTING.md
├─ LICENSE.md
├─ README.md
