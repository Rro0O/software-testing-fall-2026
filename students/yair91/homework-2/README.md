# Homework 2: Testing Concepts Analysis

**Student**: Emmanuel Arias
**GitHub username**: `yair91`
**Application**: Aula — Student Management System (Option B, hypothetical)
**Date**: September 5, 2026

## Summary

This submission designs a risk-based test strategy for Aula, a hypothetical student management system for a mid-sized university. The strategy concentrates effort on the four functions whose failure is irreversible — access control, grade and transcript accuracy, enrollment concurrency and payment processing — and treats everything else in proportion. It covers ten test types, the four testing levels, the seven testing principles, and a risk matrix of ten entries with an explicit testing priority order.

## Why this application

A student management system is a system of record rather than a product people use for entertainment. Its output is a legal document, it operates under privacy obligations, and it faces one extreme load peak per term on a date fixed by the academic calendar. Those constraints make the difference between a critical defect and an inconvenient one unusually clear, which is what the analysis is built around.

## Contents

1. [Part 1 — Application analysis](part1-application-analysis.md)
2. [Part 2 — Testing types](part2-testing-types.md)
3. [Part 3 — Testing levels](part3-testing-levels.md)
4. [Part 4 — Testing principles](part4-testing-principles.md)
5. [Part 5 — Risk analysis and prioritization](part5-risk-analysis.md)

## At a glance

| Part | Requirement          | Delivered     |
| ---- | -------------------- | ------------- |
| 1    | 300+ words           | 725 words     |
| 2    | 8+ test types        | 10 test types |
| 3    | 4 testing levels     | 4 levels      |
| 4    | 7 testing principles | 7 principles  |
| 5    | 6+ risks             | 10 risks      |
