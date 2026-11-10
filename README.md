# devops-ci-app

Учебное Flask-приложение для практической работы № 10.

Автор: Аникеев Егор Александрович
Группа: ЭФБО-03-24

CI: Pylint → pytest → Docker build → smoke-test → GHCR.

Публикация образа выполняется только из `main`.
В Pull Request выполняются проверки без публикации.

- health endpoint: `/health`;
- образ: `ghcr.io/eeegggooorrr1/devops-ci-app`;
- основной workflow: `.github/workflows/ci.yml`.
