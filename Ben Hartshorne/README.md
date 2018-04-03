
# Test in Production: From End to End Checks to Observability

## Description

"This workshop is intended to help developers think about what their code does after they push to production. It’s intended to start a conversation with folks who don’t identify as SREs or ops folks, about correctness, reliability, and observability into their systems.

The goal of the workshop is for attendees to leave knowing how to begin instrumenting and investigating app behavior in production.

Outline:

Talk/intro: What does uptime even really mean? Why are we content with writing integration tests and relying on exception trackers to tell us that everything’s okay in production? Let’s look at what it means to bring production closer to our test and development environments, and why end-to-end checks can be so valuable.
Introduce the first activity: describe our Rails setup (a Phillips Hue bulb, in the front of the room, may be involved), and identify (quickly) the traditional ways we’ve verified correctness in our code: unit tests, integration tests, etc. Ask the room whether the definition of “correctness” in an integration test matches the real-world, production version.
Activity time: walk through writing an e2e check together for the server. Note that - for some participants - their e2e check fails. Use as an opportunity to discuss the need for greater insight into what’s happening on production (and why exception trackers might not be enough).
Live coding/lecture time: we add instrumentation to a few key spots in the Rails setup. This will include a conversation about how to think about adding instrumentation specific to the problem we’re trying to solve, and what sorts of business-relevant attributes are useful for debugging in general.
Activity time: participants run their e2e checks again, and we try to identify the root cause of failed e2e checks from the graphs/visualizations of the instrumentation we just did. We’ll talk about what to look for when tracking down weird behavior in production and specific instrumentation patterns that help with identifying specific problems."

## Prerequisites

Before attending please install Docker for Mac or Docker for Windows via https://docs.docker.com/install/#cloud


