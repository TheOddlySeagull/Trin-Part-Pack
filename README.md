<div align="center">

# Trin Part Pack — Engines, Wheels, Seats, More

Immersive Vehicles (MTS/IV) parts pack providing engines, wheels, seats, crates, decor, and crafting elements used by Trin packs.

</div>

[![Discord](https://img.shields.io/badge/Discord-join-7289DA?logo=discord&logoColor=white)](https://discord.gg/ujQR3wf)
[![Build Status](https://github.com/TheOddlySeagull/Trin-Part-Pack/actions/workflows/build.yml/badge.svg)](https://github.com/TheOddlySeagull/Trin-Part-Pack/actions/workflows/build.yml)

## Overview

The Trin Part Pack supplies the reusable parts required by Trin vehicle and content packs. Many Trin vehicles won’t spawn without this pack installed.

- Required by: Trin Civil Pack, others
- MC versions targeted: 1.12.2 and 1.16.5

## Download

- GitHub Actions artifacts: each CI run uploads JARs for 1.12.2 and 1.16.5.
- Releases: push a tag (e.g., `v2.27.1`) to trigger a release with attached JARs.

## Requirements

- Minecraft with Immersive Vehicles (MTS/IV)
- This pack’s JAR in your `mods` folder

## Installation (Players)

1. Install Immersive Vehicles (MTS/IV).
2. Download the Trin Part Pack JAR for your MC version.
3. Place it into your `mods` folder.
4. Launch the game.

## Building (Developers)

Prereqs:
- JDK 8
- Git and Gradle wrapper (included)

Quick build:
- Windows: `gradlew.bat buildForge1122 && gradlew.bat buildForge1165`
- Linux/macOS: `./gradlew buildForge1122 && ./gradlew buildForge1165`

Artifacts appear under `out/`.

CI:
- GitHub Actions builds on push/PR, uploads artifacts, and publishes releases on tags.

## Changelog

See [CHANGELOG.md](./CHANGELOG.md) for version history.

## License & Credits

- Content and branding © TheOddlySeagull and contributors. All rights reserved unless otherwise stated.
- Immersive Vehicles by its respective authors.

## Community

- Discord: https://discord.gg/ujQR3wf
- Issues: Use this repo’s Issues for bugs and feature requests.

