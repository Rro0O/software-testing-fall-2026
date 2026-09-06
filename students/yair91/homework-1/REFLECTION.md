# Reflexión — Homework 1

## Retos que enfrenté

El reto no fue Git en sí, sino romper la costumbre de trabajar sobre `main` cuando el proyecto es mío y nadie más lo va a tocar. Llevo años entregando en ramas en el trabajo, pero casi nunca me detengo a planear cómo va a quedar el historial. Aquí tuve que decidir de antemano qué iba en cada rama y qué merecía un commit propio, y eso obliga a pensar antes de escribir. Lo más incómodo fue el conflicto de merge: creé `feature/add-content` a partir de `feature/initial-structure` antes de integrar `feature/add-styling`, y ambas ramas agregaron una fila a la misma tabla del README. Provocarlo a propósito y resolverlo con calma resultó más útil que evitarlo.

## Comandos más útiles

`git log --oneline --graph --all` fue el que más me sirvió, porque deja ver la forma del historial en lugar de imaginarla. `git status` y `git diff --staged` antes de cada commit, para no arrastrar cambios que no correspondían. `git checkout -b <rama> <base>` para ser explícito sobre de dónde sale cada rama, que fue justo lo que provocó y después explicó el conflicto. Y `git merge main` dentro de la rama antes de abrir el pull request, para resolver los conflictos en local y no en la interfaz de GitHub.

## Historial y estrategia de ramas

La práctica completa está en <https://github.com/yair91/git-workflow-practice>: cuatro ramas de característica, catorce commits convencionales y cuatro pull requests con descripción, todos mergeados a `main`.

## Aplicación en el proyecto de equipo

Partiré siempre de un `main` actualizado, con una responsabilidad por rama, y abriré el pull request con contexto suficiente para que alguien más pueda revisarlo sin preguntarme nada. Resolver los conflictos en local antes de pedir revisión es lo que me llevo como hábito.
