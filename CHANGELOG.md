# Changelog
This is a list of changes that have been made between releases of the ``evaluation-instruments`` library. See GitHub for full details.

Breaking changes may occur between minor versions prior to the v1 release; after which API changes will be restricted to major version updates.

<!-- towncrier release notes start -->

## 0.0.2

### Features

- Add 5cs evaluation instrument ([#11](https://github.com/epic-open-source/evaluation-instruments/issues/11))
- Establish pattern for interchangeable instruction sets, to allow score-only or score+explanation output formats ([#10](https://github.com/epic-open-source/evaluation-instruments/issues/10))

### Bugfixes

- Update default postproccessing to handle the objects returned by more providers ([#7](https://github.com/epic-open-source/evaluation-instruments/issues/7))
- Update the results transform to handle single score objects ([#7](https://github.com/epic-open-source/evaluation-instruments/issues/7))
- Update decorator to use pathlib not os ([#7](https://github.com/epic-open-source/evaluation-instruments/issues/7))

### Changes

- Adding a ``MANIFEST.in`` to ensure the entire ``instruments/`` folder is included in pip-installed distributions ([#9](https://github.com/epic-open-source/evaluation-instruments/issues/9))
- Update the explanation response to be a dictionary instead of list ([#10](https://github.com/epic-open-source/evaluation-instruments/issues/10))

## 0.0.1

### Features

- Adds PDSQI-9 instrument prompt and example notebook. ([#2](https://github.com/epic-open-source/evaluation-instruments/issues/2))
- Adds the initial dataset evaluation handling and decorators for integrating prompts with it. ([#2](https://github.com/epic-open-source/evaluation-instruments/issues/2))
- Adds summary of inpatient care and clinical denial appeal instrument prompts and example notebooks. ([#6](https://github.com/epic-open-source/evaluation-instruments/pull/6))
