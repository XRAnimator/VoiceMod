<img src="./.github/assets/app-icon.png" alt="Voice Assistant App Icon" width="100" height="100">

# Web Voice Assistant

This is a starter template for [LiveKit Agents](https://docs.livekit.io/agents) that provides a simple voice interface using the [LiveKit JavaScript SDK](https://github.com/livekit/client-sdk-js). It supports [voice](https://docs.livekit.io/agents/start/voice-ai), [transcriptions](https://docs.livekit.io/agents/build/text/), and [virtual avatars](https://docs.livekit.io/agents/integrations/avatar).

This template is built with Next.js and is free for you to use or modify as you see fit.

![App screenshot](/.github/assets/frontend-screenshot.jpeg)

## Getting started

> [!TIP]
> If you'd like to try this application without modification, you can deploy an instance in just a few clicks with [LiveKit Cloud Sandbox](https://cloud.livekit.io/projects/p_/sandbox/templates/voice-assistant-frontend).

Run the following command to automatically clone this template.

```bash
lk app create --template voice-assistant-frontend
```

Then run the app with:

```bash
pnpm install
pnpm dev
```

And open http://127.0.0.1:3000 in your browser.

You'll also need an agent to speak with. Try our [Voice AI Quickstart](https://docs.livekit.io/start/voice-ai) for the easiest way to get started.

> [!NOTE]
> If you need to modify the LiveKit project credentials used, you can edit `.env.local` (copy from `.env.local.example` if you don't have one) to suit your needs.

## Password Protection

This frontend now includes password protection to prevent unauthorized access. To configure:

1. Copy `.env.local.example` to `.env.local`
2. Set `LIVEKIT_ACCESS_PASSWORD` to your desired password
3. Share this password only with authorized users

Users will need to enter the password before they can start a conversation. The default password is `voicemode123` but you should change this for production use.

## Contributing

This template is open source and we welcome contributions! Please open a PR or issue through GitHub, and don't forget to join us in the [LiveKit Community Slack](https://livekit.io/join-slack)!
