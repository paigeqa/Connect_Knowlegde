# ProtoPie Docs — 99 pages



---

---
title: "AI Document Q&A"
url: https://www.protopie.io/learn/docs/ai/ai-document-qna
---

# AI Document Q&A

# AI Document Q&A

## Overview

AI Document Q&A helps you find answers about ProtoPie Studio features, formulas, and documentation without leaving your workspace. Ask questions in natural language and get instant, relevant answers with code examples and resource links.

## What You Can Ask

- How to use specific triggers, responses, or formulas

- Formula syntax and examples

- Feature explanations and best practices

- Diagram generation with Mermaid

## Example Prompts

- "How do I create a scrolling interaction?"

- "Explain the indexOf function"

- "Show me tutorials about variables"

- "Draw a user flow diagram of this prototype using Mermaid"

## Using Code Examples

When AI provides formula code:

1. Review the code explanation

1. Click **[Copy]** to copy the formula

1. Paste it into your formula field in Studio

1. Adjust variable names to match your prototype

Example formula response:

```html
// This formula checks if the email field contains an "@" symbol, returning true if valid. indexOf(`Email field`.text, "@") > -1
```

## Resource Cards

Documentation responses include interactive resource cards:

### **Document Cards**

- Title with document icon

- Link path (e.g., "Getting Started | Formulas | ProtoPie Guide")

- Preview description

### **Video Cards**

- Video thumbnail with play icon

- Video title and description

- Link to YouTube or tutorial platform

## Limitations

AI Document Q&A:

- Searches ProtoPie's official documentation only

- Cannot access your specific project files or custom workflows

- May not have information about very recent feature updates during beta

- Provides guidance but cannot directly modify your prototype (use AI Interaction Creation for that)


---

---
title: "AI Interaction Creation"
url: https://www.protopie.io/learn/docs/ai/ai-interaction-creation
---

# AI Interaction Creation

# AI Interaction Creation

## Overview

AI Interaction Creation enables you to build interactions using natural language, eliminating the need for manual configuration of triggers and responses. Describe what you want to happen, and Studio AI will generate the appropriate interaction logic.

## How It Works

1. Open the AI panel

1. Type your interaction request in natural language

1. Use **@ mentions** to reference specific layers for better precision

1. AI analyzes your workspace, plans the interaction, then executes step-by-step

1. Review the results and refine manually if needed

## Example Prompts

**Basic interactions:**

- "Change @Button color when tapped"

- "Navigate to Scene 2 when @Card is clicked"

- "Make @Layer draggable horizontally only"

**Complex interactions:**

- "Add a Stop and Start interaction that changes the color and text of the button on the right. Also start and stop the timer accordingly."

- "If email is invalid, change button to gray"

- "Create a toggle. First tap shows panel, second tap hides it"

## Understanding AI's Process

When you enter a prompt, Studio AI:

1. **Analyzes your workspace:** Reviews selected layers, existing variables, and scene context

1. **Plans the interaction:** Shows you a summary of steps it intends to execute

1. **Executes step-by-step:** Creates triggers, responses, and formulas while highlighting affected layers

1. **Confirms completion:** Shows completion status and offers options to revert if needed

## Context Awareness

Studio AI understands your workspace context:

- **Selected layers:** References the layer you have selected

- **Existing variables:** Reuses variables when appropriate instead of creating duplicates

- **Scene structure:** Understands layer hierarchy and grouping

- **Previous interactions:** Remembers earlier requests within the same session

## Working with AI Results

![Working With AI](https://cdn.sanity.io/images/vidqzkll/production/0184f9f97268e3fdbf873d4241ae755f0654d02b-1920x1080.gif/Working with AI.gif)

**Reviewing generated interactions:**

- AI-created elements are highlighted on the canvas with a colored border when mentioned

- The Properties panel shows all interaction details

- You can expand/collapse AI's explanation sections in the chat

**Editing and refining:**

- All AI-generated interactions are fully editable through Studio's interface

- Make changes in the Properties panel, Interaction panel, or directly on canvas

- AI will recognize your manual edits and respect them in subsequent requests

## Stopping and Reverting

**Stop:** Click **[Stop]** during execution to cancel. Changes will be reverted automatically.

**Revert:** After completion, click **[Revert]** to undo AI's most recent changes. Revert is available until you manually edit the canvas.

**What happens when you stop:**

- If stopped after tasks complete: Retains edits, task block freezes

- If stopped during tasks: Reverts edits, brings back prompt input

## Limitations

During the beta period, AI Interaction Creation:

- **No VLM:** AI cannot "see" visual design on canvas, but it reads layer structure and property data only

- Creates interactions for existing layers (does not generate new designs or layouts)

- May require refinement for very complex conditional logic

- Cannot create or modify interactions within components

- Chat history is not saved across sessions


---

---
title: "AI Panel Interface"
url: https://www.protopie.io/learn/docs/ai/ai-panel-interface
---

# AI Panel Interface

# AI Panel Interface

## Panel States

The AI panel displays different states during operation:

**Idle State:** Ready for your input. When there's no chat history, four suggested prompts are displayed to help you get started. Ready for your input. When there's no chat history, four suggested prompts are displayed to help you get started. Click a suggested prompt to populate the input field. Prompts are entered but not automatically submitted.

**Processing State:** AI is analyzing your request. You'll see status indicators like "Fetching..." or "Analyzing..."

**Editing State:** AI is actively modifying your prototype. A banner appears at the bottom of the canvas showing "ProtoPie AI is taking control" with a **[Stop]** button to cancel if needed.

## Chat Behavior

- Submitted prompts appear at the top of the chat area

- Chat history is **not saved** across sessionsâclosing the tab or resetting clears history

- To start fresh, click the reset button in the panel header

## Using @ Mentions

Type **@** to mention specific layers in your prompt. This provides better context to the AI and generates more precise interactions compared to describing layers by name alone.

Example: "Make @ButtonLayer turn gray when tapped"

## Response Controls

After AI responds, you have several options:

**ð / ð Feedback:** Rate response quality to help improve the AI.

**Copy Response:** Copies the entire response content (including code blocks) to your clipboard.

**Rewrite:** Regenerates a different response for the same prompt.

- Only available for the latest response

- Disappears if you send a new prompt or make manual edits

## AI Response Types

Studio AI provides different response formats depending on your request:

### Text Responses

Plain text explanations with formatting support, including headers, body text, links, inline code, blockquotes, and tables. Used for explanations, documentation answers, and general responses.

### Mermaid Diagrams

AI can generate visual diagrams using Mermaid.js syntax when you ask it to draw flowcharts, user flows, or other diagrams. The flowcharts are based on existing objects and interactions from the workspace. Diagrams render as interactive images with options to:

- **Copy code:** Copy the Mermaid.js source code

- **Download as image:** Save the rendered diagram as .svg

### Formula Blocks

Code blocks specifically for ProtoPie formulas, displayed with:

- Syntax highlighting

- **Copy** button

- **How to use** link to ProtoPie formula documentation

### Code Blocks

General code examples (JSON, JavaScript, etc.) with language label, syntax highlighting, and **Copy** button.

### Resource Cards

When AI references documentation, it displays interactive resource cards:

**Official Articles:** ProtoPie icon, article title and breadcrumb path, "Official Article" label

**YouTube Videos:** Video thumbnail, "Youtube Video" label

**External Links:** Globe icon with URL

Multiple resources display in a carousel with pagination.

### Plan Block

For interaction creation, AI shows its planning process:

**While planning:** Displays "Planning..." with expandable content showing the full analysis.

**When complete:** Collapses to "Planned" with checkmark. Content includes:

- **Goal:** What AI intends to create

- **Structure:** Elements to be used

- **Creation Order:** Step-by-step execution plan

- **Interactions:** Trigger â Response mapping

### Task Block

Shows execution progress for interaction creation:

**In progress:** "Working..." with spinning icon

**Done:** "X tasks done" with checkmark

Each task shows the action type (Add, Edit, Delete, etc.) and affected elements. Checkmarks indicate completed tasks, spinners show in-progress tasks.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/ai/getting-started
---

# Getting Started

# AI

â ï¸ **Beta Notice**

> Studio AI is currently in beta. Features may change, and functionality is being continuously improved based on user feedback.

## What is Studio AI?

Studio AI is ProtoPie's AI-powered assistant that helps you create interactions and get answers about Studio features through natural language. Start fast with AI, then refine every detail with ProtoPie's signature manual control.

## Key Features

![Interaction Creation](https://cdn.sanity.io/images/vidqzkll/production/ddb232a97b286aa2e548c4cce10372f92c5bea40-1920x1080.gif/Interaction Creation.gif)

**Interaction Creation:** AI creates triggers, responses, and conditional logic using natural language commands. Describe what you want, and AI generates the appropriate interaction logic.

![Document Q&A](https://cdn.sanity.io/images/vidqzkll/production/8e11df41a97620b44c720e381fc39c0c27e7ff2e-3828x2160.png/Document Q&A.png)

**Document Q&A: **Get instant answers about Studio features, formulas, and documentation without leaving your workspace. Includes code examples and resource links.

![Full Manual Control](https://cdn.sanity.io/images/vidqzkll/production/ab6a641c9997befe5ea5b80938b08b6b1c8b1f3e-1920x1080.gif/full manual control.gif)

**Full Manual Control:** All AI-generated content remains fully editable through Studio's traditional interface. AI generates the initial version, and you refine the final interaction.

## Accessing Studio AI

![Accessing ProtoPie AI](https://cdn.sanity.io/images/vidqzkll/production/9b02d19b3a315a2afbcf198c51b1d6f8465c38a2-3828x2160.png/Accessing ProtoPie AI.png)

Studio AI is available in the right-side panel of ProtoPie Studio:

1. Open ProtoPie Studio

1. Look for the **"AI"** button in the right panel

1. Click the AI button to open the AI panel, or use the keyboard shortcut **â/** (Mac) or **Ctrl+/** (Windows)

You can resize the panel by dragging the left edge, or detach it into a floating window to view properties and the AI panel simultaneously.

## Requirements & Availability

**Availability:** Basic, Pro, and Enterprise plans ([view pricing](https://www.protopie.io/pricing))

**Before you start:**

- **Basic & Pro:** Save your Pie to Cloud first. AI features use your team's shared AI credit.

- **Enterprise:** AI features are disabled by default â contact your organization admin to enable access.


---

---
title: "Tips for Best Results"
url: https://www.protopie.io/learn/docs/ai/tips-for-best-results
---

# Tips for Best Results

# Tips for Best Results

ProtoPie AI works best when it can reference **existing, clearly-defined elements** in your design.

## Prepare Your Elements First

- Create all necessary layers (text, shapes, images, etc.) before asking the AI

- Include initial content that reflects the intended behavior

  - Example: "0" for a counter display, "OFF" for a toggle label

## Use Descriptive Layer Names

- Rename layers to reflect their purpose

  - â "counterDisplay" instead of "Text 1"

  - â "submitButton" instead of "Rectangle 3"

- Clear naming helps AI understand your intent and reduces errors

## Use @ Mentions

Reference layers directly with @ mentions for better precision:

- â "Make @submitButton turn gray when tapped"

- â "Make the submit button turn gray"

## Be Specific in Your Requests

**Instead of:** "Make a counter."

**Try:** "When the Start trigger fires, increment the counter variable and display it in the @counterDisplay text layer."

## Describe Interactions Clearly

- **Specify triggers:** "on tap," "on drag," "on scroll," etc.

- **Define start and end states:** Clearly state the beginning and ending values (position, opacity, scale, etc.)

- **Include timing:** Duration, delay, or easing curves when relevant

## Break Down Complexity

- Don't try to do everything in one requestâbreak it down and make multiple simpler requests

- Use follow-ups to refine results by asking AI to adjust what it just created

## Verify Results

- Preview interactions to confirm behavior

- Double-check generated formulas for edge cases

- AI creates the first version, you perfect the final behavior


---

---
title: "Auto Layout Properties"
url: https://www.protopie.io/learn/docs/auto-layout/auto-layout-properties
---

# Auto Layout Properties

# Auto Layout Properties

Auto Layout provides extensive customization options for structuring layouts, ensuring both functionality and aesthetic appeal. These properties include resizing, direction, layout alignment, and advanced settings.

## Resizing Properties

Resizing properties control how child layers and their parent containers adjust in response to content or layout changes. These settings can be applied individually for Width and Height using the dropdown menus in the right panel. Hovering over a resizing option highlights its effect on the canvas.

### Fixed 

When the **Fixed** option is set for either width or height, the parent frame retains its absolute size regardless of any resizing of the child layers.

### Hug Contents

When the **Auto Layout (AL)** parent is set to **Hug**, the parent frame dynamically adjusts its size to perfectly fit the dimensions of its child layers.

### Fill Container

When a child is set to **FILL**, its size adjusts to fill the available space within the parentâs dimensions, making it relative to the parentâs size.

## Direction Properties

Direction properties define how child objects are arranged within an Auto Layout container, providing flexibility in structuring layouts for various design scenarios.

## Layout Properties

Layout properties offer granular control over child layer Alignment, Padding, and Gap within an Auto Layout container. These settings ensure a polished and consistent design.

## Auto Layout and Constraints

When a **container without Auto Layout** wraps a **child container with Auto Layout**, specific interactions occur depending on vertical or horizontal constraints.

### **Vertical Constraints**

If the Auto Layout container has **Top & Bottom (T+B)** or Scale assigned to it, the Auto Layout containerâs height must be Fixed. Changing the Auto Layout container back to **Hug** resets the vertical constraints to **Center**.

### **Horizontal Constraints**

When the Auto Layout container has **Left & Right (L+R)** or **Scale** assigned to it, the Auto Layout containerâs width is set to **Fixed**. Adjusting the Auto Layout container to **Hug** resets the containerâs horizontal constraints to **Center**.

These adjustments ensure a logical interaction between Auto Layout and non-Auto Layout containers, offering a predictable workflow.

## Advanced Settings

Auto Layout also provides additional advanced settings to enhance layout flexibility and customization. These options allow you to tailor specific elements and behaviors within your design.

### Ignore Auto Layout

The "Ignore Auto Layout" feature allows you to bypass auto layout rules for selected objects, enabling manual adjustments without affecting the overall container structure. Objects set to âIgnore Auto Layoutâ can independently set constraints, providing flexibility for unique layout scenarios while maintaining the auto layout properties of other elements in the container.

![Ignore Auto Layout](https://cdn.sanity.io/images/vidqzkll/production/1aa652aa062db0d6187304d3f001ce4d57f82dc3-650x516.png/image (10).png)

### Layer Order Control

Managing stacking order is made simple with multiple options:

- **Layer Panel**: Drag layers directly in the panel to reorder them.

- **Keyboard Shortcuts**: Adjust stacking order using arrow keys for precise layer control.

- **Mouse Interaction**: Click and drag objects on the canvas to reposition them interactively.

### Instance Overrides

Instances of components with Auto Layout support selective adjustments, allowing flexibility without altering the master component.

- **Resizing:** Modifications to resizing values are limited to existing options; new fixed values cannot be added.

- **Alignment, Gap, and Padding:** These properties are customizable within instances.

- **Direction:** Directional changes are not supported in instances.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/auto-layout/getting-started
---

# Getting Started

# Auto Layout

Auto Layout in ProtoPie Studio is designed to automate alignment and spacing, simplifying layout creation and adjustment. By transforming regular containers into Auto Layout Containers, it ensures consistency and flexibility throughout the design process.

![Auto Layout](https://cdn.sanity.io/images/vidqzkll/production/deb962dc340634e7ebc6503981ab1592afa897b7-2010x960.png/Auto Layout.png)

## Difference Between Fixed Layout & Auto Layout

Fixed Layout and Auto Layout provide different ways to handle alignment and spacing in design.

- **Fixed Layout**: Requires manual adjustments to maintain consistency, offering precise but static control.

- **Auto Layout**: Dynamically adapts to content changes, reducing manual effort and enabling responsive designs.

## Getting Started with Auto Layout

You can enable Auto Layout for containers, components, or multiple objects using the Property Panel, right-click menu, or a simple shortcut. Once applied, Auto Layout automatically assigns default properties.

### ****How to Apply Auto Layout

You can enable Auto Layout via:

- **Property Panel**: Select a layer or container and check the Auto Layout option.

- **Right-Click Menu**: Right-click and select "Add Auto Layout."

- **Shortcut**: Use the `Shift+A` shortcut.

![Apply Auto Layout](https://cdn.sanity.io/images/vidqzkll/production/f48959a87033d2fadf64b1d4d74268d6abc8a853-1722x934.png/Add auto layout.png)

When you apply Auto Layout, the following **default properties** are assigned:

- **Direction**: Vertical

- **Resizing**: Hug Contents for both width and height

- **Alignment**: Top-Left

- **Gap**: 10px

- **Padding**: 10px (applied uniformly to all sides)

### Auto Layout Visibility in the Property Panel

The Auto Layout option becomes visible in the Property Panel depending on the selected layer type or group. Hereâs how it works for different cases:

- **Single Container**: Enable Auto Layout for a container to transform it into an Auto Layout container.

- **Main Components**: Apply Auto Layout to components for consistent behavior across instances.

- **Multiple Objects**: Add Auto Layout to multiple selected objects, grouping them into a single Auto Layout container.

### How to Remove Auto Layout

You can restore manual control over alignment and spacing by disabling Auto Layout. This feature allows you to switch back to Fixed Layout when needed.

You can remove Auto Layout via:

- **Property Panel**: Uncheck the Auto Layout option.

- **Right-Click Menu**: Select "Remove Auto Layout."

- **Shortcut**: Use `Option+Shift+A` (Mac) / `Alt+Shift+A` (Windows).

![Remove Auto Layout](https://cdn.sanity.io/images/vidqzkll/production/96909a38c40342bc460004df314a975d2fb9e7da-1722x934.png/Remove Auto Layout.png)

## **Notes on Auto Layout**

While Auto Layout is powerful and flexible, there are a few things to keep in mind to make the most of this feature. Here are some important points about how Auto Layout interacts with specific layers:

- **Mask Layers**: Applying Auto Layout to a mask layer replaces the mask option with Auto Layout.

- **Audio Layers**: Auto Layout does not affect resizing or interactions with audio layers.

- Auto Layout can be applied to **single non-container layers**, but only via shortcuts or the right-click menu. It is not accessible in the Property Panel.


---

---
title: "Containers"
url: https://www.protopie.io/learn/docs/basic-features/container
---

# Containers

# Container

Use containers to group two or more layers and apply actions to the whole group. Containers also enable scrolling and paging interactions.

### Relative Coordinates

By default, a layer's x and y coordinates are calculated from its upper left corner relative to the scene. However, the coordinates of a layer inside a container are always calculated based on its upper left corner relative to the parent container.

![relative coordinates](https://cdn.sanity.io/images/vidqzkll/production/a012b4216524fcb68d6fe71a8d8dfb7b7cd33a27-1580x480.png/image.png)

### Clip Sublayers

The **Clip Sublayers** option in the property panel allows you to hide the content outside of the top layer's bounding box.


---

---
title: "Devices"
url: https://www.protopie.io/learn/docs/basic-features/devices
---

# Devices

# Devices

Create prototypes in ProtoPie Studio for a variety of devices and device frames. Choose from the most popular devices for iOS, iPadOS, Android, and desktop. Or set up a custom size for all other screen types.

The resolutions in the following list refer to portrait mode.

## Mobile & Tablet

By default, prototypes for iOS, iPadOS, and Android display their respective device frames when previewed on the cloud.Â [Learn more](https://www.protopie.io/learn/docs/cloud/getting-started)Â about ProtoPie Cloud.

### iOS & iPadOS

Here is a list of the iOS & iPadOS devices that ProtoPie supports: 

- iPhone 14 Pro Max â 430 x 932 px

- iPhone 14 Pro â 393 x 852 px

- iPhone 14 Plus â 428 x 926 px

- iPhone 14 â 390 x 844 px

- iPhone 13 Pro Max â 428 x 926 px

- iPhone 13/13 Pro â 390 x 844 px

- iPhone 13 Mini â 375 x 812 px

- iPhone 12 Pro Max â 428 x 926 px

- iPhone 12/12 Pro â 390 x 844 px

- iPhone 12 Mini â 375 x 812 px

- iPhone 11 Pro Max â 414 x 896 px

- iPhone 11 Pro/X â 375 x 812 px

- iPhone 11 â 414 x 896 px

- iPhone 8 â 375 x 667 px

- iPhone 8 Plus â 414 x 736 px

- iPhone SE â 320 x 568 px

- iPhone 7 â 375 x 667 px

- iPhone 7 Plus â 414 x 736 px

- iPad Pro â 1024 x 1366 px

- iPad â 768 x 1024 px

### Android

Here is a list of the Android devices that ProtoPie supports: 

- Samsung Galaxy S20Â âÂ 360 x 800 px

- Samsung Galaxy S10 âÂ 360 x 760 px

- Samsung Galaxy S8/S9 â 360 x 740 px

- Samsung Galaxy S7 âÂ 360 x 640 px

- Samsung Galaxy Note 5 â 360 x 640 px

- Google Pixel 5 â 393 x 851 px

- Google Pixel 4XL âÂ 411 x 869 px

- Google Pixel 4 âÂ 393 x 829 px

- Google Pixel 3 âÂ 411 x 822 px

- Google Pixel 2 âÂ 411 x 822 px

- Google Pixel â 411 x 371 px

- Google Nexus 6P âÂ 411 x 731 px

## Desktop, Web & TV

Find below the device sizes that ProtoPie supports for desktop, web, and TV: 

- Desktop â 1280 x 1024 px

- Desktop HD âÂ 1440 x 1024 px

- HD 720p â 1280 x 720 px

- HD 1080p âÂ 1920 x 1080 px



## Selecting a Device

![selecting-a-device](https://cdn.sanity.io/images/vidqzkll/production/a9e7ecb69185b3fa105e4a9664d6dee5806361ec-1526x954.gif/select device.gif)

1. Click on the **device name** in the toolbar.

1. Choose the desired type of device in the **Select Device** menu.

1. Select the device.

1. Choose the orientation.

### Orientation

Choose between two types of orientation:

- Portrait

- Landscape



## Customizing a Device

If you can't find the device size you need for your prototype, you can set up a custom device size.

1. Click on **Custom** within the **Select Device** menu.

![customize devices](https://cdn.sanity.io/images/vidqzkll/production/ed15a271f7c665a7592697cc9483b9d7cd5756da-725x368.png/customize-device.png)

1. Enter the desired **Width** and **Height** values.

1. Fill in **Density** (screen pixel density: @2x, @3x, @4x, etc)

1. Optionally, activate the device's System Status Bar.


---

---
title: "Layers"
url: https://www.protopie.io/learn/docs/basic-features/layers
---

# Layers

# Layers

ProtoPie allows you to use layers for shapes like rectangles, ovals, stars, and polygons, as well as media like images, videos, and Lottie animations. 

### Layer Properties

## Image Layer

You can seamlessly integrate and refine images within your prototype with the Image layer. ProtoPie supports the following image formats: PNG, JPG, JPEG, BMP, GIF, SVG, and WebP.

### How do you add image layers?

There are two ways to add image layers to your project. The first one is to drag and drop the image onto the scene. The second way is to create an image layer and select an image by setting the fill property. To maintain the image's original dimensions, click the 'Apply original ratio' option in the property panel. 

Depending on your plan, you can import images from your local files or, for Enterprise users, from a [self-hosted URL](https://www.protopie.io/learn/docs/basic-features/layers#supported-media-file-format).

Fine-tune various aspects such as opacity, radius, fill, and more directly from the Properties panel to achieve the desired visual effects.

### SVG Layer

In ProtoPie, you can import Scalable Vector Graphics (SVG) and edit their properties by converting them to shapes using the 'Make Editable' option without losing quality.

- When working with SVG files that ProtoPie doesn't fully support, the 'Make Editable' button could change how the layers look.

- Color gradients and multi-color fills are currently not supported.

- You can copy SVG code from Sketch, Figma, Adobe XD, or Zeplin and paste it directly into ProtoPie.

Import vector layers as SVG with the [ProtoPie plugin for Figma.](https://protopie.io/learn/docs/basic-features/import#figma-import-plugin)

![svg layer convert to shape](https://cdn.sanity.io/images/vidqzkll/production/dd6d73e1590f9fd10de2399b6410194d553b0cd3-771x441.png/CleanShot 2023-12-19 at 21.17.23.png)

## Video Layer

You can add videos by dragging and dropping them onto the scene or by creating a video layer and selecting your preferred video. If you want to maintain the original dimensions of the video, you can click on the 'Apply original ratio' option in the property panel.  

Depending on your plan, you can import videos from your local files or, for Enterprise users, from a [self-hosted URL](https://www.protopie.io/learn/docs/basic-features/layers#supported-media-file-format).* *

ProtoPie supports MP4 (H.264), WebM, and MOV video files up to 100 MB. However, before importing your video into ProtoPie Studio, it is crucial to ensure that your video meets specific criteria for seamless testing with ProtoPie Player on mobile devices:

**For iOS:**

- Supported formats include MP4 (H.264) and MOV. 

  - M4V, MP4, MOV file formats encoded with H.265/H.264 video, up to 4K/60 fps, High Profile level 4.2 with AAC-LC audio up to 160 Kbps, 48kHz, stereo audio.

  - M4V, MP4, MOV file formats encoded with MPEG-4 video up to 2.5 Mbps, 480p/30 fps, Simple Profile with AAC-LC audio up to 160 Kbps, 48kHz, stereo audio.

  - AVI file formats encoded with Motion JPEG (M-JPEG) up to 35 Mbps, 1280 by 720 pixels, 30 frames per second, audio in ulaw, PCM stereo audio.

- Reference: 

  - [Apple AVFoundation AVFileType Documentation](https://developer.apple.com/documentation/avfoundation/avfiletype)

  - [Apple AVFoundation AVVideoCodecType Documentation](https://developer.apple.com/documentation/avfoundation/avvideocodectype)

**For Android:**

- Supported formats include MP4 (H.264) and WebM.

- Reference:

  - [Android Supported Media Formats](https://developer.android.com/guide/topics/media/platform/supported-formats)

### Video with Transparent Background

By supporting videos with transparent backgrounds, ProtoPie takes a pioneering step towards 3D while enhancing the performance of your prototypes.

Before importing your video into the ProtoPie Studio scene, verify that the video codec and format meet the below criteria to ensure optimal performance within their designated platform, whether the Preview window, ProtoPie Player, or ProtoPie Cloud.

Transparent background videos perform at their best under the following conditions:

- **For the Web**: Chrome supports VP9 with alpha (.webm), and Safari supports HEVC with alpha (.mov, *.mp4).

- **For iOS**: It's recommended to use HEVC with alpha. Incorrect codec/format on iOS may lead to content not displaying correctly within the designated area.

- **For Android**: Android does not natively support video files with alpha channels.

## Lottie Layer

A Lottie media layer loads a JSON file containing parsed Adobe After Effects animations exported with Bodymovin.Â Learn moreÂ about [LottieFiles](https://lottiefiles.com/what-is-lottie).

You can add Lottie files by dragging and dropping them onto the scene or by creating a Lottie layer and selecting your preferred Lottie file. If you want to maintain the original dimensions of your Lottie file, you can click on the 'Apply original ratio' option in the property panel.

 Depending on your plan, you can import Lottie files from your local files or, for Enterprise users, from a [self-hosted URL](https://www.protopie.io/learn/docs/basic-features/layers#supported-media-file-format).

## Audio Layer

ProtoPie supports WAV, MP3, and M4A audio files.

## Camera Layer

You can use the output from your smart device's native camera as a layer in your prototype and even [scan QR and barcodes](https://www.protopie.io/blog/qr-code-scanner). This only works when you test the prototype using ProtoPie Player. A placeholder is shown instead when you run the prototype in the preview window or web browser.

## Text Layer

A text layer is a layer that displays a text. 

### Missing Font

If a font is missing, a missing font warning will show. Select alternative fonts to replace the missing fonts.

![missing font panel](https://cdn.sanity.io/images/vidqzkll/production/7349203da8b42c524fb67bb4a5a69f0e097a9c51-1054x920.png/image.png)

### Applying Custom Fonts to a Text Layer

*Available in the Enterprise plan only.*

Editors can easily apply custom fonts to text layers in ProtoPie Studio by following these simple steps:

1. Select an editable text layer.

1. Access the Font menu located in the text layer's property panel.

1. Browse through the fonts list and select one of the custom fonts available within the âCustomâ category. The list exclusively displays the custom fonts accessible within your enterprise team and/or organization.

1. The selected text layer will now be displayed with the chosen custom font.

Note: Only the [team owner](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin#managing-fonts),  [team admins](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin#managing-fonts), and [service admins](https://www.protopie.io/learn/docs/enterprise/service-admin#removing-custom-fonts-from-proto-pie-cloud) can upload custom fonts.

![Applying Custom Fonts to a Text Layer](https://cdn.sanity.io/images/vidqzkll/production/52a5b50e17fbda0b6e1a5762e74208f7325340dd-2000x1103.png/studio_custom.png)

### Applying Custom Fonts to All Text Layers with the Same Font

*Available in the Enterprise plan only.*

Editors can effortlessly apply custom fonts to all text layers that share the same font across all scenes in the prototype by following these steps:

1. Click on "Edit" in the top navigation menu.

1. Choose "Replace Fonts" from the options.

1. In the Replace Fonts modal, choose the font(s)  you want to replace with a custom font.

1. Click on the âReplaceâ button.

1. The selected font(s) will be replaced with the chosen custom font(s) throughout the prototype.

![Applying Custom Fonts to All Text Layers with the Same Font](https://cdn.sanity.io/images/vidqzkll/production/f353397b8822ee8a74d980476c25eb70f139feee-2000x1103.png/studio_replace.png)

## Input Layer

An input layer is used to enter single-line or multi-line text via a native keyboard on smart devices or a physical keyboard.

### Background Blur Layer

The following blur effects are supported: three default effects (*Dark*, *Light*, and *Extra Light*) for Android and iOS and ten more blur effects for Web and iOS 13 and newer.

### Constraints

You can set constraints for layers. The size and position of child layers adjust automatically according to their constraints when the parent layer is resized manually or through a [Response](https://www.protopie.io/learn/docs/interactions/responses). 

#### Pin to Top Right Corner

By setting a Right and Top constraint, the grey layer would maintain its position relative to the right and top sides of its parent layer. Additionally, if the parent layer is resized, the grey layer maintains its size.

#### Scale Spacing

By setting the Scale option for both width and height, the grey layerâs size and position adjust proportionally to changes in the parent layerâs size, maintaining the same scaling ratio as the parent.

#### Fixed Spacing

By setting L+R in the width and T+B in the height, the grey layer would be resized maintaining the same spacing left and right when the parent layer's width is modified.  

## FAQs


---

---
title: "Preview Window"
url: https://www.protopie.io/learn/docs/basic-features/recording
---

# Preview Window

# The Preview Window

![the preview window](https://cdn.sanity.io/images/vidqzkll/production/7025643019f88db60de38a0a69e47ae0666f7131-2000x1288.png/preview.png)

To view your interactions in action and identify any errors before sharing your prototype, use the preview window. The preview window updates automatically when changes are made to layers or interactions. If you prefer to hide the preview window when opening ProtoPie Studio or switching between prototypes, simply toggle it off in **Preferences**.

## Recording Interactions

ProtoPie makes it simple to capture your prototypes in action. With just a click, you can easily record your prototype directly from the preview window. You have up to 5 minutes to capture everything you need. Your recordings will be saved in the popular MP4 (H.264) format, making it easy to share and view.

![Recording in Preview mode in ProtoPie Studio.](https://cdn.sanity.io/images/vidqzkll/production/864eea99fa6d58ba454b018f796ba9f76618f9f0-2175x1200.png/Recording in ProtoPie Studio.png)

Before you use this feature, make sure to authorize ProtoPie to record your screen. Head over to your computer's **Security & Privacy **settings and grant permission. Once you've done that, you'll be all set to capture your prototypes in action with ease.

![Enabling screen recording.](https://cdn.sanity.io/images/vidqzkll/production/fcb24de86eacdb844e563358597807d93a2bfd6b-2175x1200.png/Enabling screen recording.png)

## Audio Recording

Record your prototype's media sounds and voice interactions using an external microphone. Click the Settings icon in the Preview window and choose the desired audio input device.

![audio recording in preview](https://cdn.sanity.io/images/vidqzkll/production/515428b5cedce83f40327b817a53d1e8760fd66d-2000x1103.png/audio-recording_(1).png)


---

---
title: "Scenes"
url: https://www.protopie.io/learn/docs/basic-features/scenes
---

# Scenes

# Scenes

A scene in your design project is similar to an artboard in Sketch and Adobe XD and a top-level frame in Figma. To adjust the size of your scene, you can either choose a device from the [Select Device](https://www.protopie.io/learn/docs/basic-features/devices) menu or enter a custom size.

Note that there are certain limitations on how many scenes you can add per prototype based on your plan. For more information, you can refer to our [feature comparison table](https://www.protopie.io/plans).

![scenes](https://cdn.sanity.io/images/vidqzkll/production/9f411af5090c7053da7de7365588ec9689a68901-2175x1200.png/Scenes.png)

### Navigating between Scenes 

ProtoPie's scenes are not displayed side-by-side as in most design tools. In ProtoPie you always edit scenes individually. 

- To open a specific scene, select it from the [Scenes Panel](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface#2-scene-panel). 

- To connect scenes, use theÂ [Jump response](https://www.protopie.io/learn/docs/interactions/responses#jump).

## Rulers & Guides

It can be difficult to align objects, shapes, or text layers on the canvas. This is where rulers & guides come in handy. These visual tools are now here to help you quickly and precisely align objects, measure distances, and prototype faster.

### Showing/hiding rulers

Rulers appear at the top and left sides of your canvas area in ProtoPie Studio. First, make sure to enable rulers & guides in [**Labs**](https://www.protopie.io/blog/discover-protopie-labs). To show/hide rulers, use Shift + R, or select **Show/Hide Rules** under View in the application menu.

![Use Shift + R, or access this under View in the application menu.](https://cdn.sanity.io/images/vidqzkll/production/5da2f11efe4871254ff04ea6e08aab91e3fb9e9e-1450x800.png/Enabling rulers.png)

### Creating guides

To create a vertical or horizontal guide, hover the mouse over the ruler area, then simply drag and drop the resize cursor.

![You can create vertical or horizontal guides by simply clicking either ruler.](https://cdn.sanity.io/images/vidqzkll/production/8a78dba1739a3363154a915fbcc2f40912a06212-1165x583.gif/Creating guides.gif)

Removing guides is simple. You can do this in three ways.

1. Select a guide and press **Delete**.

1. Drag the guide back to the ruler area.

1. Go to View and select **Clear Guides**.

![Select Clear Guides under View in the application menu to remove all guides.](https://cdn.sanity.io/images/vidqzkll/production/341f96f6f99a46ca1a7eaffc56b4259c67af5a76-1450x800.png/Clear guides.png)

The guides will remain active even after saving and quitting the prototype. However, they will not display upon opening an entirely new tab.


---

---
title: "Scroll/Paging"
url: https://www.protopie.io/learn/docs/basic-features/scroll-paging
---

# Scroll/Paging

# Scroll / Paging

You can adjust the scrolling or paging properties of a container from its [Property panel](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface#4-property-panel). To enable scrolling or paging layers inside a container, drag them into the target container from the [Layer panel](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface#1-layer-panel). 

## Scroll

This option enables horizontal or vertical scrolling. To make sure your scroll interactions work flawlessly, make sure the child layers extend beyond the bounding box of the scroll container.

### Properties

## Paging

Paging refers to a container that snaps to the equivalent of its height or width, depending on the chosen direction (horizontal or vertical). 

### Properties

## Scroll & Paging Use Cases

Learn how to effectively utilize scroll and paging for common scenarios. Discover how to create vertical and horizontal scroll views for mobile and desktop applications. Gain insights into correctly configuring scroll properties and selecting the right triggers and responses for scroll-related interactions.

Experience the prototypes firsthand and download them to examine their interactions. Additionally, explore our tutorials to understand the step-by-step process behind creating each prototype.

Find the use case you need below:



- [Browsing through a social media app](https://www.protopie.io/learn/docs/basic-features/scroll-paging#browsing-through-a-social-media-app)

- [Vertical scroll in a messaging app](https://www.protopie.io/learn/docs/basic-features/scroll-paging#vertical-scroll-in-a-messaging-app)

- [Looping scroll carousel](https://www.protopie.io/learn/docs/basic-features/scroll-paging#looping-scroll-carousel)

- [Wheel picker](https://www.protopie.io/learn/docs/basic-features/scroll-paging#wheel-picker)

- [Scrolling & paging from the middle](https://www.protopie.io/learn/docs/basic-features/scroll-paging#scrolling-paging-from-the-middle)

- [Infinite paging scroll](https://www.protopie.io/learn/docs/basic-features/scroll-paging#infinite-paging-scroll)

### Browsing through a Social Media App

Like most social media apps function these days, you can make a horizontal and vertical scroll to browse through different profiles and photos. Learn how to add margins to the scroll views to maintain a similar UI (spaces at the end of the scroll) as in your apps.

![browsing through a social media app](https://cdn.sanity.io/images/vidqzkll/production/510ba8c6fb2b643e42ccb78c4d0561654bb66640-1450x990.gif/Messaging app.gif)

[Try the prototype](https://cloud.protopie.io/p/00779d40ec?_ga=2.268075918.1643676014.1632367973-92142306.1630233724) yourself.

[Learn](https://www.protopie.io/blog/how-to-create-a-nested-scroll) how to create this prototype step-by-step.

### Vertical Scroll in a Messaging App

Scroll up and down to see messages in a messaging app or email inbox. Create a scroll container and learn how to set a custom starting scroll position (for example, from the bottom). 

![vertical scroll in a messaging app](https://cdn.sanity.io/images/vidqzkll/production/299066208ecc7e05bfaf3fb2110e411ffafcecd4-1450x990.gif/vertical scroll messaging app.gif)

[Try the prototype](https://cloud.protopie.io/p/4f6d51846e?_ga=2.99337374.1643676014.1632367973-92142306.1630233724) yourself.

[Learn](https://www.protopie.io/blog/prototype-a-scroll-view) how to create this prototype step-by-step.

### Looping Scroll Carousel

As in online shopping websites or a gallery of images on video streaming platforms, you can create a slideshow. Learn how to use theÂ paging container to make a carousel view and how to use variables to alternate image names while scrolling. 

![looping scroll carousel](https://cdn.sanity.io/images/vidqzkll/production/7267ce1f05a44631d8cc46fb749ce3481a3a528a-1450x990.gif/Untitled.gif)

[Try the prototype](https://cloud.protopie.io/p/813641dff6?_ga=2.3416880.1643676014.1632367973-92142306.1630233724) yourself.

[Learn](https://www.protopie.io/blog/how-to-create-a-looping-scroll-carousel) how to create this prototype step-by-step.

### Wheel Picker

Make your own wheel picker to pick a date, time, etc. A wheel picker allows you to scroll up and down through multiple choices very quickly. It is useful, especially when the list of options cannot be fully displayed because they may exceed the available space on your screen. 

![wheel picker](https://cdn.sanity.io/images/vidqzkll/production/bd8591114fb705fdb5bb563f349f27f71aeeeefa-1450x965.gif/Wheel picker.gif)

[Try the prototype](https://cloud.protopie.io/p/780f41920c?_ga=2.266481550.1643676014.1632367973-92142306.1630233724) yourself.

[Learn](https://www.protopie.io/blog/how-to-create-a-scrolling-wheel-picker-with-3D-Rotate) how to create this prototype step-by-step.

### Scrolling & Paging from the Middle

Allow your pages to scroll from the middle to both left and right. Learn how to set up the right container property to make it happen. 

![scroll paging from the middle](https://cdn.sanity.io/images/vidqzkll/production/5d73e733580fe358b8b95064f70e0f00f09d6407-1450x990.gif/Scroll paging from the middle.gif)

[Try the prototype](https://cloud.protopie.io/p/cc3fd6271b) yourself.

[Learn](https://www.protopie.io/blog/paging-tip) how to create this prototype step-by-step.

### Infinite Paging Scroll

Make your pages scroll infinitely in both directions. Learn how to group pages using a paging container and use the range trigger to enable the infinite scroll. 

![infinite paging scroll](https://cdn.sanity.io/images/vidqzkll/production/9c1813bf653cc535c4cf283c6042a01b8392096b-1450x990.gif/infinite paging scroll.gif)

[Try the prototype](https://cloud.protopie.io/p/b2cf26584b) yourself.

[Learn](https://www.protopie.io/blog/looping-animation-tip-part-two) how to create this prototype step-by-step.


---

---
title: "Shortcuts"
url: https://www.protopie.io/learn/docs/basic-features/shortcuts
---

# Shortcuts

# Shortcuts

Save time and boost your productivity with ProtoPie's keyboard shortcuts!

Here's a list of all the shortcuts you can use to navigate and work faster in ProtoPie. You can also find them in the **Shortcuts** modal inside ProtoPie Studio by opening the Help menu or using the shortcut â + â§ + / (on macOS) or Ctrl + â§ + / (on Windows).


---

---
title: "System Status Bar"
url: https://www.protopie.io/learn/docs/basic-features/system-status-bar
---

# System Status Bar

# System Status Bar

This option allows you to display the native system status bar when previewing prototypes on mobile devices. It has to be activated in the [scene](https://www.protopie.io/learn/docs/basic-features/scenes)âs property panel. The system status bar displays according to the chosen [device](https://www.protopie.io/learn/docs/basic-features/devices). It can also be used with a custom device size.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/cloud/getting-started
---

# Getting Started

# ProtoPie Cloud

ProtoPie Cloud is a web-based platform that allows you to store, manage, handoff, and share your ProtoPie prototypes. With customizable links, [interaction recordings](https://www.protopie.io/learn/docs/interaction-recordings/getting-started), and the ability to let stakeholders experience prototypes on their own devices, ProtoPie Cloud offers a comprehensive solution for prototype testing and sharing.

## Opening Cloud Pies in ProtoPie Studio

The prototypes stored on your cloud can be opened directly from ProtoPie Studioâs dashboard.

If you canât find your cloud-stored prototype under Recent Pies, you can open it by clicking the** Open Pie** button.

![opening-pies-in-the-cloud](https://cdn.sanity.io/images/vidqzkll/production/dc30949c8d2f2aa9054c952ffc4c5f3433855ff9-1450x950.gif/opening-prototypes-from-cloud.gif)

You can directly open a Pie in ProtoPie Studio from the Pie Cloud page by clicking on the Pie name and choosing "Open in Studio."

![open cloud stored pie in studio](https://cdn.sanity.io/images/vidqzkll/production/bb0239c4365c7905f4e8a25a3b11186062c2afbe-1881x1139.png/CleanShot 2023-12-19 at 20.16.41.png)

## Uploading Prototypes

Follow these steps to upload prototypes to the cloud from ProtoPie Studio:

1. Click the **Cloud** button in the upper right corner.

- If you are on the Pro or Enterprise plan, you can choose between saving prototypes locally (âOn My Computerâ) or uploading them to the cloud (âSaveâ).

- If you are on the Free or Basic plan, you can save your prototypes **only **on the cloud.

![upload-pies-to-cloud](https://cdn.sanity.io/images/vidqzkll/production/34cd0a0fe4b35c71564680a5075fee977de1caf1-1450x860.png/upload-pie-to-cloud.png)

     2.  Choose where the file should be saved (**personal** or **team** space). If you choose a team space, select the right project and click **Save**.

![choose-project-space-cloud](https://cdn.sanity.io/images/vidqzkll/production/1971f9441a8d61886d2b9982b4de7f2ec3abe95c-1450x860.png/projects-cloud.png)

     3. The prototype's cloud link will display once the upload is complete. Click on the link to preview your prototype on the cloud or select **Copy **to share the link with others. You can customize the sharing options on the prototype's page. 

Learn more about [sharing prototypes](https://www.protopie.io/learn/docs/cloud/sharing-prototypes). 

![copy-pie-link](https://cdn.sanity.io/images/vidqzkll/production/f130403a6225777a00280affc31027ebb60a7c56-1450x360.png/copy-link-pie.png)

You can upload your Pie as a new prototype or overwrite an existing one.

![overwrite-pie-in-the-cloud](https://cdn.sanity.io/images/vidqzkll/production/251dc8b1d3493e09bab533d2520a54e0f5f3d32d-1450x760.png/overwrite-pie-in-cloud.png)

Uploading a Cloud Pie through the Cloud button automatically overwrites the version stored on the cloud. To overwrite another prototype on the cloud click on **Save As** under File and choose the prototype that needs to be overwritten.

To remove Pie files from your Recent Pies list, click **Remove from recent**. To delete prototypes from your computer or the cloud, click **Delete**.

![removing-pie-from-recent-files](https://cdn.sanity.io/images/vidqzkll/production/72703de660b21d1e3d7377c73cbff70f390560eb-2175x1200.png/removing-from-recent.png)

You can manage the information and settings of a prototype on the cloud, including renaming it and restoring older versions.

[Learn more](https://www.protopie.io/learn/docs/cloud/managing-prototypes)[** **](https://www.protopie.io/learn/docs/cloud/managing-prototypes)about managing prototypes.

## Testing Prototypes

You can easily share the link of your prototype with stakeholders. Depending on the prototype, they can preview it on web browsers or the Player app. [Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes)Â about sharing prototypes.

### Testing Prototypes on Desktop Browsers

ProtoPie cloud links can be opened on any major desktop browser (e.g. Google, Safari, Firefox). There are various display options you can choose from. Open **View Options** to customize how your prototype is displayed on web browsers. 

![pie-page-cloud](https://cdn.sanity.io/images/vidqzkll/production/3a57c22a0365550f20de2c72bd0f42d1b8c2f9d0-1679x1114.png/CleanShot 2023-12-19 at 18.06.24@2x.png)

Right-click the background of the prototype page to access additional options, such as Full Screen, ProtoPie UI, and so on.

![additional-view-options-in-the-cloud](https://cdn.sanity.io/images/vidqzkll/production/d5ef972e1c65aef126354ab049a6a220d315c9f9-1624x1462.png/CleanShot 2023-12-19 at 18.07.18@2x.png)

### Testing Prototypes on Mobile Browsers

You can conveniently open and test prototypes directly on mobile browsers. However, it's important to note there are certain limitations when using prototypes in mobile browsers.

The [input layer](https://learn/docs/basic-features/layers#input-layer), sensor-related interactions, and [voice prototyping](https://learn/docs/voice-prototyping/getting-started) features may not function as intended. We recommend opening the prototype in ProtoPie Player to use these features fully.

### Testing Prototypes with ProtoPie Player

[Video: Cloud > Open in mobile - Video](https://www.youtube.com/watch?v=xY0-93CuSgE)

ProtoPie Player is a powerful companion app designed to test and run prototypes on iOS, iPadOS, and Android devices.

ProtoPie Player ensures a seamless testing experience, free from the limitations that may arise when using mobile or web browsers.

To experience the full range of features and functionalities of your prototype, open ProtoPie Player and scan the QR code of the prototype stored in the cloud. Alternatively, you can enter the shareable link provided.Â [Learn more](https://www.protopie.io/learn/docs/player/getting-started)Â about testing prototypes in ProtoPie Player.


---

---
title: "Managing Prototypes"
url: https://www.protopie.io/learn/docs/cloud/managing-prototypes
---

# Managing Prototypes

# Managing Prototypes

On ProtoPie Cloud, you can manage your prototypes' information and settings, edit their name and description, adjust access settings, and easily access previous versions.

Ready to share your prototypes?Â Learn moreÂ about [sharing prototypes](https://www.protopie.io/learn/docs/cloud/sharing-prototypes).

## Updating Prototype Information

1. Click on the name of your prototype. An overflow menu will appear, offering various options.

1. Select **Show Pie information** from the menu to access the prototype details.

1.  Click the pencil icon next to the description field to modify the description.

1. If you want to rename a prototype, click on **Rename** from the overflow menu.

![protopie cloud changing information](https://cdn.sanity.io/images/vidqzkll/production/45e0f1aa21488f759d5863ecdbb9a7279eb34cfc-1679x1114.png/CleanShot 2023-12-19 at 20.24.05@2x.png)

## Managing Version History

The version history feature lets you keep track of various iterations of your prototype.

1. Click on the name of your prototype and select **Show version history**.

1. In the cloud, your prototype's version history is readily available. The latest version will be displayed by default.

1. Hover over the latest version to view its date and time.

1. To access a specific version,  click on the corresponding date and time.

![check prototype version history](https://cdn.sanity.io/images/vidqzkll/production/84bb98b4d62d33f462917b80668d9fd170809dd5-1679x1114.png/CleanShot 2023-12-19 at 20.26.18@2x.png)

Each version offers the following options:

- **Download**: If you prefer to work with the prototype in ProtoPie Studio,  download the Pie file.

- **QR Code**: Scan the QR code to open the prototype in ProtoPie Player. For Enterprise users, ensure you log into Player using your enterprise account to access the Pie file on the Enterprise Cloud.

- **Delete**: You can remove a specific version by deleting it.

## Duplicating & Moving Prototypes

Duplicating or moving prototypes within ProtoPie Cloud is easy. Whether you're duplicating or transferring prototypes between different projects or spaces, we've got you covered.

Learn more about [spaces](https://release-docs.protopie.io/learn/docs/teams/getting-started#spaces) in ProtoPie Cloud.

### Duplicating Prototypes

![duplicating-prototypes](https://cdn.sanity.io/images/vidqzkll/production/b145ac4966ac833b3cf5e01a547856c1075adaf5-1679x1114.png/CleanShot 2023-12-19 at 20.30.11@2x.png)

In your personal space, you can duplicate any prototype hassle-free. For team spaces, only editors with project access can duplicate the prototypes inside the project.

When you duplicate a prototype, you automatically become the owner of the new copy. Duplicates are always created in the same personal space or project as the original prototype.

### Moving Prototypes

It is possible for owners and editors who have access to a project to move prototypes within it. However, if you are a viewer or do not have access to a project, you cannot move its prototypes.

You can move a prototype from your personal space to a project within a team spaceand move prototypes across projects within a single team space. However, please note that moving prototypes between team spaces is not supported.


---

---
title: "Managing Storage"
url: https://www.protopie.io/learn/docs/cloud/managing-storage
---

# Managing Storage

# Managing Cloud Storage

On ProtoPie Cloud, you can easily monitor and manage your storage usage. This includes handling interaction libraries and revision history. Follow these steps to keep your cloud storage optimized.

## Viewing Storage Usage

To check your storage usage, go to the **âStorageâ** menu. Hereâs how the information is presented based on your plan and role:

**For Free/Basic plans:**

Youâll see your personal storage capacity, with a list of Pies sorted from largest to smallest by size.

**For Pro/Enterprise plans:**

- **Viewers:** The view is the same as for Free/Basic plan users unless you have a basic subscription.

- **Members:** Youâll see your top three projects by storage size, including project and editor names. You can also access the "Manage Revision History" menu.

- **Admins/Owners:** Admins can switch views between teams using the Global Navigation Bar (GNB) if you are managing multiple teams.

![Pro Plan_Viewing Storage Usage](https://cdn.sanity.io/images/vidqzkll/production/4b757e670d94e510d7197268b26fbb28b8a2db55-1284x922.png/Storage Documentation 01.png)

## Managing Revision History

The revision history feature lets you track and manage previous versions of your prototypes.

1. Go to the **âStorageâ** menu and select **âManage Revision Historyâ** from the Pie list.

2. You will be directed to the Pieâs revision history tab, where you can:

- View and manage different versions of your prototype.

- Delete revisions individually to ensure clarity on what is being removed.

- Resources (images, videos, etc.) associated with a deleted revision will be cleared from storage unless they are being used by other revisions.

![Managing Revision History 01](https://cdn.sanity.io/images/vidqzkll/production/914baccfce856cd9004eee649932507700441c83-1440x1024.png/Revision history.png)

![Managing Revision History 02](https://cdn.sanity.io/images/vidqzkll/production/10434f55655893f39a639eed35405ca14be2dd23-1440x1024.png/Revision history (1).png)

### Handling Private Projects

This section applies to Pro or above plan users:

**Team Admin & Editors:** Private Projects are shown as "Private Project" with hidden names and editor details. The "Manage revision history" menu is disabled.

**Service Admin:** You can see the names of Private Projects and Editors but not the names of the Pies. The "Manage revision history" button is disabled.

![POR 2.0 Private Project](https://cdn.sanity.io/images/vidqzkll/production/72cfcefa58ca7fcb9110fc1bcb5e65f32a028780-1408x1012.png/Private Project_Editors.png)

## Managing Cloud Storage Limits

On ProtoPie Cloud, understanding what happens when you reach your storage limit helps you take timely action to manage your storage effectively. Hereâs what you need to know about handling storage limitations and managing uploads.

### General Scenario: Uploading a New or Changed Pie

### **If storage was not yet maxed out:**

If you had some available storage space before the upload (e.g., a Pro user with 4.98 GB used out of 5 GB), ProtoPie Studio will allow the save. However, you will receive a notification indicating that your storage is nearing its limit. You will need to manage your storage from the Cloud page.

![Storage capacity warning](https://cdn.sanity.io/images/vidqzkll/production/899d853ad6ad4a0a7e2a4df564f459d840ddbbf7-556x370.png/Storage Capacity Warning.png)

### **If storage is already exceeded:**

**Free/Basic plans:** 

You will not be able to upload new or updated Pies if your storage limit has been exceeded. You must free up space or upgrade your plan to continue saving new files.

**Pro plans:** 

- **Team Members:** If your storage limit is exceeded, you cannot upload new or changed Pies. You need to either manage your storage by deleting unnecessary files or contact your service admin for additional storage options.

- **Team Admins:** If the team adminâs own storage or the overall team storage is maxed out, they will not be able to upload new or changed Pies. They should review and manage storage across all teams and projects, or [**contact us**](https://www.protopie.io/form/enterprise-plan-contact-us) to request additional storage.


---

---
title: "Sharing Prototypes"
url: https://www.protopie.io/learn/docs/cloud/sharing-prototypes
---

# Sharing Prototypes

# Sharing Prototypes

Sharing your prototypes with others is a seamless process in ProtoPie. You have full control over who can access your prototypes and how they are displayed when shared. 

Also, you can pair your prototype with an [interaction recording](https://www.protopie.io/learn/docs/interaction-recordings/creating-interaction-recordings) to give engineers all the interaction specifications they need for development.

## Managing Prototype Access

When you're ready to share a prototype, click the** Share** button in the upper right area of the page. You can choose who can view and download the prototype, giving you full control over its accessibility.

![protopie-cloud-share-settings](https://cdn.sanity.io/images/vidqzkll/production/dcd17ec1d19dc2dd5a6364ad5bc1944acd116964-1679x1114.png/CleanShot 2023-12-19 at 18.10.14@2x.png)

### Allowing Anyone

By choosing this option, you allow anyone who receives the prototypeâs link to view and/or download the prototype.

![anyone-with-the-link-share](https://cdn.sanity.io/images/vidqzkll/production/d363714902cc8f25d6c848e67ee155e246881ea4-1679x1114.png/CleanShot 2023-12-19 at 18.11.51@2x.png)

### Access Level

When sharing prototype links with stakeholders, you can customize the level of access using the Access Level menu. Here are the available options:

- **Can view & download:** Anyone who receives the prototype's link can both view and download the prototype.

- **Can view:** Anyone who receives the prototype's link can only view the prototype without the ability to download it.

- **Can view prototypes only:** This option is ideal for user testing as it simplifies the process of sharing and accessing prototype links. However, it doesnât allow you to customize how the prototype displays on web browsers. For more customization, use the above options.

- **No access:** The prototype remains inaccessible to anyone outside of your team space.

![pie access level ](https://cdn.sanity.io/images/vidqzkll/production/d0898cb844003ce20735a746dcfe604e04b1de47-1950x1474.png/CleanShot 2023-12-19 at 18.12.45@2x.png)

### Allowing Team Members

*Pro and Enterprise plans only.*

![only-team-members](https://cdn.sanity.io/images/vidqzkll/production/b4d04799862717b0baf5141fa2a9e6de2c0fcba5-1856x1462.png/CleanShot 2023-12-19 at 18.13.53@2x.png)

You can restrict access to your prototype exclusively to members of your team space. By enabling this setting, only team members can access the prototype.

### Password Protection

Sharing prototypes externally can raise concerns about unauthorized access. To address this, we offer password protection, which adds an extra layer of security to your shared prototypes.

By enabling password protection, you can ensure that only individuals with the correct password can access your prototypes.

![password-protection](https://cdn.sanity.io/images/vidqzkll/production/106eb832e82ef071d8e686fe8ecada6c42b4e269-1758x1466.png/CleanShot 2023-12-19 at 18.14.46@2x.png)

1. Click on **Share** in the upper-right area of the Pie page.

1. Click on the section below the space owner's name.

1. Select **Anyone with the link & password**.

1. Type in your password.

1. Click **Save**.

### Shareable Link Expiry

*Enterprise plan only*

The Enterprise plan allows you to set an expiration for shared links of your prototypes. This ensures that the link becomes inactive and inaccessible once the specified time has elapsed, providing an added layer of protection for your sensitive designs.

This feature will become available after allowing anyone with the link to access your prototype.

You can select the expiration period for the shareable link, ranging from 1 day, 3 days, to 1 week.

![pie access link expiry](https://cdn.sanity.io/images/vidqzkll/production/0172ab71da2908b3baa47bc82834f756b49e6827-1539x970.png/CleanShot 2023-12-19 at 19.58.54@2x.png)

## Change Scene

Effortlessly navigate your prototype scenes using the "Change Scene" option. Generate dedicated links for each scene, having precise control over your sharing experience. This feature is especially valuable for designers and researchers [testing prototypes](https://www.protopie.io/learn/docs/user-testing/overview) on platforms like Maze.

![change scene](https://cdn.sanity.io/images/vidqzkll/production/c48c55efa482b8ad772311b0df3e201204fed28b-1539x970.png/CleanShot 2023-12-19 at 20.02.37@2x.png)

## View Options

To ensure that your stakeholders have the best viewing experience, ProtoPie allows you to customize the display options before sharing your prototypes.

Click on the **Gear** icon to access the display options. Choose various display options such as device frame visibility, cursor type, hotspot hints, and more.

Once you have selected the display options, share the prototype with your testers using the "Copy Link" option under Share or by copying the link directly from the address bar. When your testers open the link, they can view the prototype exactly as you intended, with all the display settings you activated.

![managing-display-options](https://cdn.sanity.io/images/vidqzkll/production/3a57c22a0365550f20de2c72bd0f42d1b8c2f9d0-1679x1114.png/CleanShot 2023-12-19 at 18.06.24@2x.png)

- **Original Size (100%)**: Display the original size of the prototype.

- **Scale to Fit**: Scale the prototype to fit within the browser.

- **Hotspot Hints:** Highlight touchable areas for easier navigation.

- **Device Frame**: Showcase the prototype within a device frame.

- **ProtoPie UI**: Include ProtoPie Cloud's interface, such as the toolbar.

- **Cursor Type**: Choose between touchpoint or arrow cursor.

- **Background**: Set a custom background color for the prototype.

- **Playback Speed**: Adjust the speed of the prototype playback.

### Sharing without Distractions

Create a focused experience for stakeholders by eliminating visual distractions. Enable **Scale to Fit** and disable** ProtoPie UI** (and optionally **Device Frame**) when sharing your prototype. 

![Share prototype without any distractions](https://cdn.sanity.io/images/vidqzkll/production/cec84fbf5f2915d3e338707d1e62d67aaa62e246-1648x1063.png/CleanShot 2023-12-19 at 18.46.35@2x.png)

### Sharing with Hotspot Hints

Simplify navigation for stakeholders by enablingÂ **Hotspot Hints**Â and highlighting touchable areas in the prototype.

![share prototype with touch hint option](https://cdn.sanity.io/images/vidqzkll/production/1494a99b1562bb3902f7f5bf3ede6878a9a8b709-2014x1462.png/touchspot.png)

### Sharing for Usability Testing

If you conduct usability testing on a desktop, you might want to share your prototype without unnecessary visual distractions.Â [Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#sharing-without-distractions)Â about how to achieve this. 

If you conduct usability testing on mobile or tablet, we recommend using [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) for a realistic experience.

## Sharing with Engineers

Enhance the development process by pairing your prototype with interaction recordings for engineers. Sharing the prototype and one or multiple interaction recordings ensures that engineers can access all the necessary interaction specs for development.

Click on the **Handoff** button to create interaction recordings that engineers can easily follow and reference during their work. This enables engineers to translate your design into a functional product accurately.

[Learn more](https://www.protopie.io/learn/docs/interaction-recipes/getting-started)Â about the handoff feature.

![sharing-with-engineers](https://cdn.sanity.io/images/vidqzkll/production/0f90807e469e42d95b5da832a3c8bb3aefce80c7-1679x1114.png/CleanShot 2023-12-19 at 18.19.05@2x.png)


---

---
title: "Component Guides"
url: https://www.protopie.io/learn/docs/components/component-guides
---

# Component Guides

# Component Guides

A component guide is a helpful document that you can create for your team members to reference when using a component from your interaction library. It allows you to provide a description and enables others to see the overridable variables, Send responses, and Receive triggers along with their corresponding messages that are utilized in the component.

## Editing Component Guides

Click the pencil icon in the property panel of the component to edit the component guide. Simple markdown is supported (except for hyperlinks, images, tables, and grammar).

![component guide editing](https://cdn.sanity.io/images/vidqzkll/production/7919070a94f461a8359a815873ed9ba4b0ca582f-1580x870.png/image.png)

### Description

Write a description about what the component is for and how it should be used.

### Variables

When a component has overridable variables, they'd be automatically displayed in the component guide. The variable type and initial value would be included as well.

![component guide variable](https://cdn.sanity.io/images/vidqzkll/production/5081d7b157ecc59ccb48d17985e578103fef3c58-1580x870.png/image.png)

### Message Out

When you use Send responses with the Send to Parent or Send to Current Scene channels, they'd be automatically displayed in the component guide.

![component guide message out](https://cdn.sanity.io/images/vidqzkll/production/94a3d31ac356ed5d93ce12ab4cb9b2a0b9b0a2bc-1580x870.png/image.png)

### Message In

When you use Receive triggers with the Receive from Parent or Receive from Current Scene channels, they'd be automatically displayed in the component guide.

![component guide message in](https://cdn.sanity.io/images/vidqzkll/production/77401f4d52ebf406f4649659872eb36a348c925e-1580x870.png/image.png)

## Previewing

When you use the component as an instance, you can see access the component guide by clicking on the component guide icon in the property panel.

![component guide preview](https://cdn.sanity.io/images/vidqzkll/production/5b6ef4ad633996df6a9cb0b76a9173e422849ca4-1580x870.png/image.png)

### Minimizing

When you use the component as an instance, you can see access the component guide by clicking on the component guide icon in the property panel.

![component guide preview minimize](https://cdn.sanity.io/images/vidqzkll/production/38bf5f6b65bf440b1810b32fa3186ea6386ad268-1580x870.png/image.png)


---

---
title: "Editing Components"
url: https://www.protopie.io/learn/docs/components/editing-components-in-a-library
---

# Editing Components

# Editing Components in a Library

To edit an instance of a component, right-click on it, click the **"Edit Main Component"** button in the property panel, or access the overflow menu of a library and select the** "Edit"** option. This action will open a new window with a purple banner indicating that you are in library edit mode.

For more details, please refer to our documentation on [ Interaction Libraries](https://www.protopie.io/learn/docs/interaction-libraries/getting-started).

![editing components in a library](https://cdn.sanity.io/images/vidqzkll/production/98f4566086d2e8f140070b84b9084c45c007662d-746x271.png/Components.png)


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/components/getting-started
---

# Getting Started

# Components

Components allow you to save sets of layers and interactions, making them reusable throughout your entire prototype. Select the layers and interactions you want to reuse, convert them into a component, and create instances across your scenes.

Here's why components are a game-changer:

- **Eliminate Repetitive Work**: Say goodbye to recreating the same elements and interactions repeatedly. Components let you create once and reuse anywhere, saving you valuable time and effort.

- **Enhance Readability**: With Components, your scenes become cleaner and easier to understand. Instead of cluttering your prototype with redundant elements, you can use instances of components for a more organized and efficient design.

- **Accelerate Workflow**: By reusing components, you can rapidly build and iterate on your prototype. Make changes to the original component, and all instances automatically update, ensuring consistency across your entire design.

## Using Components

### Creating Components in a Scene

Transforming layers into components is a breeze with ProtoPie. Follow these simple steps:

1. Select the layer(s): Choose the layer or multiple layers you want to turn into a component.

1. Click the "Component" icon: Look for the component icon in the toolbar and click it. Alternatively, you can right-click on the selected layer(s) and choose **Convert to Component** from the context menu.

1. Voila! Your component is ready: ProtoPie automatically creates a component with the selected layer(s) and their corresponding interactions. The original layers are replaced by an instance of the component.

![creating component from a scene](https://cdn.sanity.io/images/vidqzkll/production/f4ed33af24017fa028ca86f11eeb69df4558b787-2175x1200.png/creating_components_in_a_scene.png)

### Creating Components Directly

Components can also be created from scratch. Open the component panel on the left side and click the plus icon. This creates an empty component that you can start customizing.

![creating component directly](https://cdn.sanity.io/images/vidqzkll/production/c05227f24805ad148d50c78b91625b3e4e42abdd-894x700.png/image (7).png)

### Adding Component Instances

You can create an instance of a component by dragging a component from the Component panel to the canvas of the active scene.

![adding component Instances](https://cdn.sanity.io/images/vidqzkll/production/ed68643124ffe2ae6228f8743f2fb4e7bd73c3bf-1121x572.png/Adding Components.png)

## Editing Components

### Editing the Main Component

To edit a main component, you must open the component editing mode. To activate this mode, click on a component from the Component panel, or right-click on an instance of the component and select **"Edit Main Component"** from the context menu.

![editing master component](https://cdn.sanity.io/images/vidqzkll/production/f55c286911e518984fa733ab4640c080296f456f-1121x572.png/Edit Main Component.png)

Editing a main component is similar to editing a scene. You can create, modify, and delete the component's layers, variables, triggers, and responses. The changes you would make are applied to all instances of the component.

Once you have finished editing the component, you can return to the scene by clicking on the "Done" button or by clicking on the left arrow button (â) located in the top left corner of the screen. Alternatively, you can navigate to any scene by clicking on a scene in the panel.

![return to scene](https://cdn.sanity.io/images/vidqzkll/production/673e795f4995ca6f759c61ad4d6e2c016ceca73b-1121x572.png/Edit Main Component Done.png)

### Editing an Instance

In ProtoPie, modifying the sublayer properties of a component instance is a breeze. Here's how it works:

- **Override with ease:** When you change a property of a sublayer within a component instance, you're simply overriding that specific property. These overrides are unique to the instance and don't affect the main component. This allows you to customize each instance independently, giving you flexibility while maintaining the core component structure.

- **Keep changes intact:** Even if you modify the main component, the overridden properties in the instance will remain unchanged. This means you can freely experiment and iterate without worrying about losing your customizations.

- **Reset with a click**: Need to go back to the original settings? No problem! Right-click on the instance and select "Reset Overrides" from the context menu. All overrides will be cleared, and the instance will revert to its original state, mirroring the main component once again.

![editing instance](https://cdn.sanity.io/images/vidqzkll/production/008bbf1447860b58d06393bd1f75b79a1934afde-1580x870.png/image.png)

### Use as Main Component

You can link an instance of a component with its main component. This allows you to edit the main component by editing the instance without being in the component editing mode.

![link with master](https://cdn.sanity.io/images/vidqzkll/production/1e1d092d08a9d3a2271171cc538bd7ecd42a4a55-2175x1200.png/link_with_main.png)

### Variable Overrides

It's possible to override the initial values of variables. You can do so by enabling the "Make Overridable" option in the variable in the main component. After enabling, you can modify the variable value in the property panel of the component instance.

![variable overriding](https://cdn.sanity.io/images/vidqzkll/production/96065e599def016321ad4bd26cb92ab9ef23abd8-1450x800.png/overridable.png)

### **Detach Component Instance**

Detaching breaks the connection with the component and turns the instance into a container. You can do this either from the property panel or the context menu. Ensure that you have enabled the feature in [**Labs**](https://www.protopie.io/blog/discover-protopie-labs) before use.

**Detach component from the context menu**

1. Right-click on the instance

1. Click on **Detach Instance**

![Right click on a component instance, and click on Detach Instance to detach it from the component.](https://cdn.sanity.io/images/vidqzkll/production/f296578b74b47d95fa0f431499149da3870b4aaf-1450x800.png/Component Detach (1).png)

**Detach component instance from the property panel**

1. Select a component instance

1. Click on the **Detach Instance** icon in the property panel

![Click on Detach Instance in the property panel to detach an instance from its component.](https://cdn.sanity.io/images/vidqzkll/production/736a06d1eb47396b054700db32e6e7655fd80c25-1450x800.png/Component Detach - property.png)

Once the instance has been detached, the Detached_ prefix will be automatically added to the detached interactionâs name. Easily identify whether an interaction stems from a detached instance or not.

![Easily identify whether an interaction stems from a detached instance or not.](https://cdn.sanity.io/images/vidqzkll/production/885d7bf8d6f14dcbeca213154197af79e2259677-1450x800.png/Component Detach - prefix.png)

## Swap Component Instances

In the right-side property panel, you can effortlessly swap any component instance with another in just a few clicks.

![component swap component](https://cdn.sanity.io/images/vidqzkll/production/03b55001bdc3c7db29aea63d8b9a31714ef02e75-1450x800.png/swap_component_instances.png)

## Grouping Components

Groups can be created or separated using the slash "/" in the component name. For example, if the name of the first component is "Button / Primary / Normal" and the name of the second component is "Button / Secondary / Normal", they would be grouped as shown below.

![component grouping component](https://cdn.sanity.io/images/vidqzkll/production/2a817ab4b9ac5e09a16a9e176e929fbe07a8e102-680x452.png/Grouping Component.png)

### **Are you ready to take your prototyping skills to the next level?**

Join the [Digital Dashboard Masterclass](https://learn.protopie.io/course/masterclass-in-advanced-prototyping-for-digital-dashboard?__s=2hdlh416jfc4vtrb5g2a&utm_source=drip&utm_medium=email&utm_campaign=ProtoPie+School%3A+Masterclass+in+advanced+prototyping+%E2%80%94+Get+early+access%21) and gain expertise in organizing assets, creating reusable components, and implementing smart logic.

If you want to learn how to reduce work duplication, build efficiently, and scale interactions effortlessly, join the newest [Mobile Game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass).

With this advanced knowledge, you can focus on the more critical tasks and take your projects to the next level, ultimately leading to a polished and robust final product.

Don't miss this opportunity to improve your skills and become an expert in prototyping!


---

---
title: "Nested Components"
url: https://www.protopie.io/learn/docs/components/nested-components
---

# Nested Components

# Nested Components

You have the flexibility to place a component within another component, creating what is known as a nested component. This can be achieved by either directly creating a new component within the main component or by including an instance of another component. Any components can be used for nesting.

When you nest a component, it becomes the child component of the one it's placed in. Consequently, any component associated with a parent component is referred to as a nested component.

![nested-components](https://cdn.sanity.io/images/vidqzkll/production/979a4d79522b97a20b149a55e247286db3a0c354-2175x1200.png/nested-components.png)


---

---
title: "Send & Receive Messages"
url: https://www.protopie.io/learn/docs/components/send-receive-messages
---

# Send & Receive Messages

# Send & Receive Messages

Components are **isolated from each other** **and scenes**, meaning triggers and responses within a component cannot be assigned to layers and variables outside of it. The same applies to triggers and responses in a scene or nested component, which cannot be assigned to layers and variables within a component.

To overcome this limitation, you can utilize the Send response and Receive trigger. Within the component, you can send a message using the Send response, and it can be received by a Receive trigger located outside of this specific component (in a scene, parent component, or child component). This communication can also work in reverse.

Of course, it is also possible to send and receive messages exclusively within the component itself.

## Send Responses

### Send to Parent

This channel allows you to send a message from the component to a parent component or scene when there's no parent component.

![send to parent](https://cdn.sanity.io/images/vidqzkll/production/2115a41c89e2b9d4e7a29739062edba2848568d5-2175x1200.png/Send to Parent.png)



### Send to Child Component

This channel allows you to send a message from the component to a child component.

![send to child component](https://cdn.sanity.io/images/vidqzkll/production/0eec885431440cbf23736ecde89f75c276a938e3-2175x1200.png/Send to Child Component.png)



### Send to Current Scene

This channel allows you to send a message from the component to the scene where the component is used.

![send to current scene](https://cdn.sanity.io/images/vidqzkll/production/29bf4b4ae2cf770c87248cbe5a92dcae11e4fe53-2175x1200.png/Send to Current Scene.png)



### Send to Current Component

This channel allows you to send a message that remains within the component.

![send to current component](https://cdn.sanity.io/images/vidqzkll/production/aafe04eef672d1c020e8bfb65b5c347c143aa651-2175x1200.png/Send to Current Component.png)



## Receive Triggers

### Receive from Parent

This channel allows you to receive messages from a parent component or scene when there's no parent component.

![receive from parent](https://cdn.sanity.io/images/vidqzkll/production/48657f12f0e5a3caefc283d94f2d15dcdc5af253-2175x1155.png/Receive from Parent.png)

### Receive from Child Component

This channel allows you to receive messages from a child component.

![receive from child component](https://cdn.sanity.io/images/vidqzkll/production/bb7529808cdae398a4ee050bb71dfa1c08e1a545-2175x1155.png/Receive from child component.png)

### Receive from Current Scene

This channel allows you to receive a message from the scene where the component is used.

![receive from current scene](https://cdn.sanity.io/images/vidqzkll/production/b3d3a91648ab9732fd13c18f4c238783f6f220ca-2175x1155.png/Receive from current scene.png)

### Receive from Current Component

This channel allows you to receive a message that remains within the component.

![receive from current component](https://cdn.sanity.io/images/vidqzkll/production/993800e909c584c80f2319d5a7d1c6ed89a56d9f-2175x1155.png/Receive from current component.png)

### Looking to explore this feature deeper?

We recommend you joining the [Digital Dashboard Masterclass](https://learn.protopie.io/course/masterclass-in-advanced-prototyping-for-digital-dashboard?__s=2hdlh416jfc4vtrb5g2a&utm_source=drip&utm_medium=email&utm_campaign=ProtoPie+School%3A+Masterclass+in+advanced+prototyping+%E2%80%94+Get+early+access%21). This masterclass offers an in-depth exploration of the Send & Receive feature and provides you with the knowledge and skills to use it effectively.

Moreover, learn how to simplify the development of complex projects, such as games, with our recently launched [Mobile Game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass).

Don't miss out on this opportunity to understand how ProtoPieâs user-friendly approach and systematic development process make your projects becomes more manageable.


---

---
title: "API Plugin"
url: https://www.protopie.io/learn/docs/connect/api-plugin
---

# API Plugin

# Using the API Plugin in ProtoPie Connect

The API plugin lets you quickly bring real data into your prototypes by connecting them to APIs and databases. 

Unlike [Custom Plugins](https://www.protopie.io/learn/docs/connect/custom-plugins), the API plugin does not require coding skills. This plugin handles the task, either sending data to APIs or retrieving data from them and seamlessly incorporating it into your prototypes in JSON format.

## What is an API?

An API, which stands for Application Programming Interface, is a set of rules that allows different computer programs to communicate and work together. It's like a bridge that helps them share information and perform tasks without knowing all the details of how each program works. In simpler terms, APIs make it easier for software to communicate and collaborate.

## Supported API Types

With the API plugin, you can easily start API requests, whether they're GET or POST, and connect with various API types:

- **Public APIs**: This encompasses popular services like Spotify, OpenWeatherMap, YouTube, ChatGPT, live scores, and many more.

- **Internal APIs**: Connect seamlessly with your organization's systems and services.

## How to Make API Requests

Follow these easy steps to use the API plugin in ProtoPie Connect and make API requests in your prototypes.

### Step 1: Creating a Send Response in ProtoPie Studio

- Start by adding a [**Send response**](https://www.protopie.io/learn/docs/interactions/responses#send) to your chosen trigger in [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface).

- Remember to select the `ProtoPie Connect/Studio` channel,  as you usually do when passing information back and forth between ProtoPie Studio and ProtoPie Connect.

- Save your prototype. 

In [this example prototype,](https://cloud.protopie.io/p/20e828f860b8c34456583ece) we want data from the [Useless Facts API](https://uselessfacts.jsph.pl/) when you pick "Random Fact" using the toggle switch. To do this, we begin by creating a Send response with the `ProtoPie Connect/Studio` channel and a unique message value.

![Setting up Send messages to make API calls in ProtoPie](https://cdn.sanity.io/images/vidqzkll/production/9af57fad1a6925eb56ceb0d92cbac260871e14a5-5620x3378.png/send_protopie.png)

**Tip**: Watch [this free lesson](https://learn.protopie.io/course/protopie-connect) on ProtoPie School to master Send and Receive messages between ProtoPie Studio and ProtoPie Connect.

### **Step 2: Configuring API Settings within the API Plugin**

- Open your prototype in [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

- Click on `Plugin`, then select the `API` plugin from the list.

- Select one of the two HTTP request methods available: [GET or POST](https://www.baeldung.com/cs/http-get-vs-post). When making API requests, GET retrieves data from the API provider, while POST sends new data to be processed.

- Enter the correct API URL for the API you want to access. Refer to the API's online documentation to obtain the correct URL. In our example, we can see [on this page](https://uselessfacts.jsph.pl/) that the URL we need is `https://uselessfacts.jsph.pl/api/v2/facts/random`

- Include a `Header` and `Body` if the API requires it. Be sure to carefully read the documentation of your chosen API for any additional parameters needed alongside the API URL.

  - The `Header` must be formatted in JSON {}, but the `Body` doesn't always need to follow JSON {} format. You can enter the `Body` in JSON {} format if the API demands it.  

- Click the `Test Request` button to verify that the connection is working properly. If an error message appears, review the information you entered in the previous steps.

![setting up API in the API plugin in ProtoPie Connect ](https://cdn.sanity.io/images/vidqzkll/production/91a654d1d9e4900c1e08a8aac43af5f7595b9b57-5620x3378.png/api-settings-protopie.png)

### Step 3: Connecting the API with your Prototype

- Click the `Message From Pie` input field to access the list of available messages. The API plugin automatically detects the messages within your prototypes. If you donât see your message, copy and paste it from the Send response you created in Step 1.

- Enable `Override URL/Header/Body with msg value` if you need to dynamically override the APIâs URL, Header, or Body with the value of the message sent from the prototype. [Learn more](https://www.protopie.io/learn/docs/connect/api-plugin#overriding-the-api-url-header-body-with-message-values) about overriding API URL/Header/Body with message values.

- In `Message to Pie`, type in a message, which will be sent back to your prototype along with the data obtained from the API request you configured in Step 2.

- Click `Activate` to establish the connection. The plugin will initiate the API request upon receiving the corresponding message from the prototype.

![connecting a prototype to an API using ProtoPie Connect's API plugin ](https://cdn.sanity.io/images/vidqzkll/production/0333b823facc4f099dceb8d9bcf520abf862f090-5620x3378.png/connect-pie-to-api.png)

### Step 4: Creating a Receive trigger in ProtoPie Studio

- Go back to ProtoPie Studio.

- In your prototype, add a [Receive trigger](https://www.protopie.io/learn/docs/interactions/triggers#receive-trigger-properties).

- Remember to choose the `ProtoPie Connect/Studio` channel, as you did when setting up the Send response in Step 1.

- Input the same message you configured in Step 3 under `Message to Pie`.

- Activate the `Assign to Variable` option. Create a [text variable](https://www.protopie.io/learn/docs/variables/getting-started#text) and select it from the list in the Receive trigger. The information obtained from the API is now stored within this variable.

- Since API data are often returned in JSON format, utilizing the [Text response](https://www.protopie.io/learn/docs/interactions/responses#text) with a [parseJson formula](https://www.protopie.io/learn/docs/formulas/functions) is the most efficient method for incorporating API data into your prototypes.

- Save the prototype and then reload it in ProtoPie Connect. Your API-empowered interaction is now ready to be tested through ProtoPie Connect!

![setting up the receive trigger and text response to receive data from APIs in ProtoPie](https://cdn.sanity.io/images/vidqzkll/production/0a88aa67df6a7a0feffde0eb5ed9664510b45f31-5620x3378.png/receive-api-response.png)

## Overriding the API URL/Header/Body With Message Values

`Override URL/Header/Body with msg value` is used to dynamically override the APIâs URL, Header, or Body parameters with the value of the message sent from the prototype.

In [ this example prototype](https://cloud.protopie.io/p/8cbb1b86ff0749093c507d03), we used this feature to override the API URL with the value from the below Send message  in the Pie file. As a result, when you test the prototype in ProtoPie Connect and type a city into the search box, you'll see the precise weather information for that city.

![overriding the API's URL with the message sent from the prototype in ProtoPie ](https://cdn.sanity.io/images/vidqzkll/production/a13ca5a964ae7168c2c6685ca9f22ae67f86178f-4096x2462.png/override-api-url-protopie.png)

 

## Running Simultaneous API Calls

Users of Connect Core and Connect Enterprise can execute multiple API requests simultaneously using the API plugin. Connect Core has the capability to run up to three APIs (provided that no other plugin is running), whereas Connect Enterprise has no limit on the number of API calls that can run simultaneously.

To run multiple API requests simultaneously in your prototype, follow these steps:

- Open the API plugin in [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

- Click on the `+` icon situated in the upper-right corner of the API Settings window. This will open a new window where you can configure and run additional API calls simultaneously. You can also duplicate your existing APIs, to keep their original settings.

![configuring multiple simultaneous API requests in ProtoPie Connect ](https://cdn.sanity.io/images/vidqzkll/production/cd021777baf05f26806e8df98c481f2059853f34-5620x3378.png/multiple-api-requests-protopie.png)

 

## API Plugin How-To Tutorials

Discover the API plugin's key features and use cases in this how-to series.

1. [API Plugin Tutorial for Beginners](https://www.protopie.io/blog/api-plugin-tutorial-for-beginners)

1. [API Plugin Advanced Tutorial](https://www.protopie.io/blog/api-plugin-advanced-tutorial)


---

---
title: "Arduino Plugin"
url: https://www.protopie.io/learn/docs/connect/arduino-plugin
---

# Arduino Plugin

# Using Arduino with ProtoPie Connect

Create multi-screen experiences across both software and hardware thanks to ProtoPie Connectâs built-in Arduino plugin.

ProtoPie Connect supportsÂ [serial communication](https://www.arduino.cc/reference/en/language/functions/communication/serial)Â with Arduino boards. The most typical setup would be connecting the Arduino hardware to the machine where ProtoPie Connect is running via USB.

[Learn more](https://www.arduino.cc/en/Guide) about how to use Arduino.

## Connecting Arduino to ProtoPie Connect via USB

1. Select **Arduino** in ProtoPie Connectâs Plugin list.

![Connect Arduino to ProtoPie Connect](https://cdn.sanity.io/images/vidqzkll/production/4d2d9e103a796f0701cdcce18687ba475bad5841-1450x800.png/Arduino-1.png)

2. Select the desired **Port** and **Baud Rate**:

- **Port**: Select the port corresponding to your Arduino board.

![Connect Arduino: select port.](https://cdn.sanity.io/images/vidqzkll/production/b4a04fcb48f281cda451a7981dbd152d24a29d05-1450x814.png/Arduino-2.png)

- **Baud Rate**: This value determines how frequently the serial connection will be checked for updates. You can select the default value 9600.

![Connect Arduino: select the baud rate.](https://cdn.sanity.io/images/vidqzkll/production/ff9fbc8df49077247cf9f451ce384d17a411eaa4-1450x800.png/Arduino-3.png)

*Please note that the Arduino plugin works with any Micro Controller communicating via serial. For exampleâif you want to use an ESP32 microcontroller, after connecting the ESP32âyou can select the appropriate port and baud rate to open the serial port ESP32 and receive data in ProtoPie Connect.

## Using Arduino with ProtoPie Connect

ProtoPie Connect and Arduino communicate using a **Message||Value** format. If the intention is to send a message without a value, **Message** would suffice.

### Sending messages from Arduino

Use the **Serial.println()** function to send messages (and values) to ProtoPie Connect, which then communicates them to all corresponding prototypes.

In the following example, Arduino sends the message **ROTATE** and value **90** every **2 seconds** to ProtoPie Connect.

```c_cpp
void setup() {
  Serial.begin(9600);
}

void loop() {
  // Send "ROTATE" to ProtoPie
  // message: ROTATE
  // value: 90
  Serial.println("ROTATE||90");
  delay(2000);
}
```

### Sending messages to Arduino

The Arduino hardware requires a separate  code to interpret incoming messages in the **Message||Value** format.

In the below example, Arduino receives and interprets messages received from ProtoPie Connect.

```c_cpp
#include <string.h>

// Declare struct
struct MessageValue {
  String message;
  String value; // Note that value is of String type
};

// Declare function that parse message format
struct MessageValue getMessage(String inputtedStr) {
  struct MessageValue result;

  char charArr[50];
  inputtedStr.toCharArray(charArr, 50);
  char* ptr = strtok(charArr, "||");
  result.message = String(ptr);
  ptr = strtok(NULL, "||");

  if (ptr == NULL) {
    result.value = String("");
    return result;
  }

  result.value = String(ptr);

  return result; 
}

// Declare MessageValue struct's instance
struct MessageValue receivedData;

void setup() {
  Serial.begin(9600);

/*
		if you want to make waiting time for reading serial data short,
		set waiting time with `Serial.setTimeout` function.
	*/
	Serial.setTimeout(10);
}

void loop() {
// Take out strings until Serial buffer is empty
	while (Serial.available() > 0) {
// From ProtoPie Connect 1.9.0, We can use '\0' as delimiter in Arduino Serial
		String receivedString = Serial.readStringUntil('\0');

		receivedData = getMessage(receivedString);
  }

	// Do something with received message from ProtoPie Connect

	if (receivedData.message.equals("FIRST")) { // If message from ProtoPie Connect equals "FIRST" do the following 
		l1 = receivedData.value.toInt(); // receivedData.value.toInt() converts the value from ProtoPie Connect to integer type and assigns it to l1
		analogWrite(firstLED, l1); 
	} 
}
```

## Use Cases

 Try recreating the following use case to understand better how Arduino works with ProtoPie Connect.

### Control Your Home Lights

Turn the lights on and off consecutively. Test this yourself using an Arduino board connected to ProtoPie Connect.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dk7-6H6jg1jM&feature=youtu.be)

1. Add [this prototype](https://cloud.protopie.io/p/7763340ee7) to ProtoPie Connect. 
2. Set up your Arduino board and the light controls following this circuit diagram.

![Connect Arduino Use Case](https://cdn.sanity.io/images/vidqzkll/production/995439aa97f7ba1079e38b69ca48252e22270b3e-2110x1554.png/connect-arduino-usecase.png)

3. Connect your Arduino board to ProtoPie Connect.
4. Use this example code to send messages from Arduino to ProtoPie Connect.

```c_cpp
#include <string.h>

struct MessageValue {
  String message;
  String value;
};

struct MessageValue getMessage(String inputtedStr) {
  struct MessageValue result;

  char charArr[50];
  inputtedStr.toCharArray(charArr, 50);
  char* ptr = strtok(charArr, "||");
  result.message = String(ptr);
  ptr = strtok(NULL, "||");

  if (ptr == NULL) {
    result.value = String("");
    return result;
  }

  result.value = String(ptr);

  return result;
}

int firstLED = 3;
int secondLED = 5;
int thirdLED = 6;
struct MessageValue receivedData;

void setup() {
  pinMode(firstLED, OUTPUT);
  pinMode(secondLED, OUTPUT);
  pinMode(thirdLED, OUTPUT);
  Serial.begin(9600);
  Serial.setTimeout(10); // Set waiting time for serial data to 10 milliSeconds
}

void loop() {
  while (Serial.available() > 0) { // Take out strings until Serial is empty
    String receivedString = Serial.readStringUntil('\0'); // From 1.9.0 version, We can use '\0' as delimiter in Arduino Serial
    receivedData = getMessage(receivedString);
  }

  if (receivedData.message.equals("FIRST")) {
    analogWrite(firstLED, receivedData.value.toInt());
    delay(30);
  } else if (receivedData.message.equals("SECOND")) {
    analogWrite(secondLED, receivedData.value.toInt());
    delay(30);
  } else {
    analogWrite(thirdLED, receivedData.value.toInt());
    delay(30);
  }
}
```

### Surgical Robot Arm

Learn how to prototype a robot arm ([Arduino Braccio robot arm](https://store.arduino.cc/products/tinkerkit-braccio-robot)) controlled by a wireless controller.

Check out [this article](https://www.protopie.io/blog/prototyping-for-robotics) to explore the practical application of ProtoPieÂ in robotics prototyping. 

[Code used in Arduino](https://create.arduino.cc/editor/tonykim/f40afc41-f8b4-4ff9-b12a-c677db47d125/preview).


---

---
title: "blokdots Plugin"
url: https://www.protopie.io/learn/docs/connect/blokdots-plugin
---

# blokdots Plugin

# Using blokdots & ProtoPie Connect

[blokdots](https://blokdots.com/) is a code-free software to build interactive hardware prototypes with [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin).

The blokdots & ProtoPie integration is available to all users, regardless of their plan. However, when used with ProtoPie Connect, it unlocks new possibilities, such as the ability to create hardware-software interactions involving three or more devices.

The typical blokdots & ProtoPie Connect ecosystem involves:

- ProtoPie Studio, to create interactions.

- ProtoPie Connect and blokdots plugin, to enable communication between ProtoPie prototypes and blokdots app which connects to Arduino and sensors.

## Getting Set Up****

**  1. Open the Pie file in ProtoPie Connect**.****

**  2. Connect blokdots to ProtoPie Connect.**

![ProtoPie Connect status](https://cdn.sanity.io/images/vidqzkll/production/bce7abd95d31a88ba059e2d43e442957ccf606f8-2220x1414.png/pp-connect-status.png)

  1. Open the blokdots application on your computer and make sure that youâve activated the âblokdots proâ plan or start the 14-day trial.

  1. If youâre running ProtoPie Connect and blokdots on the same computer, the connection should happen automatically

  1. If youâre running ProtoPie Connect and blokdots on different computers, open the connection settings and enter the URL of the ProtoPie Connect server

Once blokdots is connected to ProtoPie Connect, the connection indicator at the ProtoPie icon in the bottom-left corner(under âConnectionsâ) should turn green. You will see a Connected message in ProtoPie Connect as well.

![blokdots plugin in connected mode.](https://cdn.sanity.io/images/vidqzkll/production/117142d1759114355b708afa1ee8bed760417f2a-1450x800.png/blokdots-1 (1).png)

  ** 3. ****Plug in the **[**Arduino board**](https://blokdots.uber.space/documentation/arduino/)**.******

![The Arduino board is ready for use.](https://cdn.sanity.io/images/vidqzkll/production/46c84354be30bd6ca596c1f7f33e49aebb249637-2175x1200.png/Connect-arduino-ready.png)

Once you see that your board is ready in theÂ top-left corner of blokdots, you can start setting up your components.

**4. Connecting the components **

This step is necessary for blokdots to know which components of the Arduino board to control.

       a. Click onÂ **Connect A New Component**Â and pick the ones you want to connect.

       b.  Chose an available Grove slot or hardware pin from the list  

c. Click onÂ **Set Component.**

![Set up your components in the Live View of the blokdots app.](https://cdn.sanity.io/images/vidqzkll/production/66d0d3b352a1effd5119a161bb961d9272c720f4-1224x698.gif/Connect-setting-up-components.gif)

  5. **Configure the components cards.**

      

    a. Start configuring each component card.

![Configure component cards in the blokdots app.](https://cdn.sanity.io/images/vidqzkll/production/b77fb204a23be42de1b7047428f0df796dce5dee-1222x697.gif/Connect-component-cards.gif)

*The blokdots app allows ProtoPie and Arduino to send messages from one to another. To make this happen, you will need to set up Send and Receive in ProtoPie Studio. To learn more about how messages are sent and received between ProtoPie and Arduino, click [here](https://www.protopie.io/learn/docs/blokdots/overview#connecting-proto-pie-with-arduino-via-blokdots).

![Setting up send and receive messages in ProtoPie Studio.](https://cdn.sanity.io/images/vidqzkll/production/a7bfe5e1fdbf598952855f28523e45dbf64c50ee-2175x1200.png/Connect-onoff-message.png)

**  6. Run the project.**

Click on the **Run** **Project** button in blokdots to run your project.

In ProtoPie Connect youâll be able to see messages coming through the blokdots plugin as you control your Arduino board.

![Messages coming through via blokdots.](https://cdn.sanity.io/images/vidqzkll/production/c10adfc267696ad3c54e4ea767ecbf1c4c80d1bc-1427x809.gif/Connect-messages-blokdots.gif)

To learn more about the blokdots and ProtoPie Connect integration, click [here](https://blokdots.com/documentation/components/integrations/protopie-connect/).


---

---
title: "Connect Embedded"
url: https://www.protopie.io/learn/docs/connect/connect-embedded
---

# Connect Embedded

# Connect Embedded

*Exclusively available as an add-on to the Enterprise plan. *

Connect Embedded is for teams who require ProtoPie Connect's functionality within embedded systems like Raspberry Pi.

It's a standalone server application that runs from a terminal and is compatible with operating systems such as Windows, MacOS, and Linux ARM64 (for Raspberry Pi). 

Connect Embedded uses a license file-based authentication and, as it can perfectly run in isolated environments, it allows for advanced product user research and testing. 

![connect-embedded-terminal](https://cdn.sanity.io/images/vidqzkll/production/61d46d8374bd306cdc2e856db187fe5489b5f597-1980x1244.png/connect embedded.png)

- **Supported Platforms:**

  - macOS10.11 El Capitan or above.

  - Windows 10 or above, 64-bit.

  - Ubuntu 12.04 or above, 64-bit.

  - Raspberry Pi OS, 64-bit

  - Fedora 221, 64-bit.

  - Debian 8, 64-bit.

- **Storage:** 500MB or more.

- **RAM:** 1 GB or more.

## Connect Desktop vs. Connect Embedded for the Enterprise Plan

The below table specifies the differences between Connect Desktop and Connect Embedded.

## Installing Connect Embedded

![Installing Connect Embedded ](https://cdn.sanity.io/images/vidqzkll/production/2ab9dc7149d7584205bc5086460d978f3c68f102-800x509.gif/install-connect-embedded.gif)

     1.   Extract the installation file required by your operating system.

  - Linux/Raspberry Pi: tar file.

  - Windows: zip file.

  - macOS: dmg file.

     2.    Move the files in the folder to the directory of your choice.

  - If you want to upgrade your Connect Embedded version, simply replace the existing files with the new ones.

## Logging into Connect Embedded

User authentication in Connect Embedded occurs through a **license file**.

- One license per each machine running Connect Embedded.

- An internet connection is not required.

- Connect Desktop and Connect Embedded cannot run at the same time. 

![connect-embedded-run-in-terminal](https://cdn.sanity.io/images/vidqzkll/production/1a3dcad9f27e316cece2b9927fae9d85d9636961-1980x1244.png/loggin into connect embedded.png)

     1.   Download ProtoPie Connect and run it from the terminal.

  - macOS:`**./pc-mac**`**,**

  - Windows: `.``**/pc-win.exe**`**,**

  - Ubuntu(intel):`**./linux-x64**` ,

  - Raspberry Pi (64bit arm): `**./linux-arm64**`

     2.   The terminal will print a **Device ID**.

     3.   Communicate the Device ID to our team when requesting access. You will be provided with a **license.txt** file.

    4.   Move the license file to the same directory where Connect Embedded is saved.

    5.   Run Connect Embedded from the terminal again, and check whether you see the following log message:Â **Licensed to YOUR NAME until YOUR EXPIRED DATE**.

    6.   Open the link displayed on the terminal in your browser or any other browser within your local area network (LAN).


---

---
title: "Custom Layer Integrations"
url: https://www.protopie.io/learn/docs/connect/custom-layer-integrations
---

# Custom Layer Integrations

# Custom Layer Integrations

ProtoPie Connect's Stage view enables you to integrate ProtoPie prototypes with diverse custom layers, including web, embeds, live cameras, and Unity projects. This integration enhances the user testing experience and renders your designs more dynamic.

## Creating a Stage View

Follow these steps to create a Stage view:

1. Open ProtoPie Connect.

1. Create a new Group and drag & drop your prototypes (Pies) into the group.

1. Select the group.

1. Click on the **View** icon to open the prototypes in a Stage.

## Embedding Custom Layers

After creating the Stage view, access the stage option menu by right-clicking. To begin editing, click the Edit button. An "Edit Mode" message will confirm that editing is enabled.

To add new prototypes or custom layers:

- From the upper-left corner, click on **Add**.

- You can include the following layers in the Stage: 

  - **ProtoPie prototypes**

  - **Web embed** via URL or iframe code (supports Maps, Spline, Rive, Bezi, etc.)

  - **Live camera** (select from available cameras or live streaming options)

  - **Unity projects** (supports import of WebGL build)

![custom layer integrations in stage view](https://cdn.sanity.io/images/vidqzkll/production/d0f1bf0370bf48c309d46b5b586b03b87f31952f-1830x999.png/stage.png)

### Configuring Web Embed Layers

You can set its URL via the properties panel after adding a new Web Embed layer to the Stage.

You can provide a full URL or iframe code. Web embeds support various formats such as Maps, Spline, Rive, and Bezi. It is important to ensure the URL is valid and you have the necessary permissions to access it.

![spline iframe embedding](https://cdn.sanity.io/images/vidqzkll/production/f72fd7677a496655770d7e10d2e4c7e39f153ced-1007x552.png/CleanShot 2024-02-27 at 17.05.17@2x.png)

### Configuring Live Camera Layers

To add camera feeds to your project, utilize the Live Camera layer. This feature supports:

- USB-connected cameras, such as webcams

- Your laptopâs camera

- Live streaming URLs (HLS)

Before using the camera layer, make sure to grant permission to your web browser. After adding the camera layer, configure its properties through the Camera properties panel.

![embed camera feeds in stage view protopie connect](https://cdn.sanity.io/images/vidqzkll/production/3d2b9cb66a97eb113771cc5e9459a4591b890769-1616x916.png/CleanShot 2024-02-27 at 17.14.13.png)

### Configuring Unity Layers

To add Unity scenes to your project, utilize the Unity layer. This feature supports:

- Importing WebGL build of Unity scenes

- ProtoPie Plugin for Unity

It is important to [build your Unity projects using WebGL](https://docs.unity3d.com/Manual/webgl-building.html) as the target platform. The resulting Build folder will contain `.loader.js`, `.framework.js`, `.wasm`, and `.data` files, which you need to archive into a zip file. Insert the zip file as a Source File to import the Unity project as a layer.

![unity layer](https://cdn.sanity.io/images/vidqzkll/production/7bbe42318cbdf41770c9887b81eb2ffd08c2f595-1440x900.png/unity.png)

The [Unity Plugin](https://www.protopie.io/learn/docs/connect/unity-plugin) will allow Send/Receive messages to work together with Unity scenes allowing for increased interactivity between the ProtoPie and Unity layers. It is a package that can be added to the Unity project and downloadable from the [Unity Asset Store](https://www.notion.so/ProtoPie-Connect-Custom-Layer-Integrations-e2b2f9e905b74d9a81f647dc03913e6d?pvs=21). For more information, refer to the [Unity Plugin](https://www.protopie.io/learn/docs/connect/unity-plugin) documentation.

## Previewing the Stage View

After adding and configuring layers, rearrange them within the Stage by dragging. To access positioning options, right-click on a layer. Preview the Stage by clicking **View** when ready.

## FAQs


---

---
title: "Custom Plugins"
url: https://www.protopie.io/learn/docs/connect/custom-plugins
---

# Custom Plugins

# Custom Plugins

Available in the Enterprise plan only.

ProtoPie Connect is equipped with several pre-installed plugins, including [API](https://www.protopie.io/learn/docs/connect/api-plugin), [IFTTT](https://www.protopie.io/learn/docs/connect/ifttt-plugin), [Logitech G29 steering wheel](https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin), [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin), [Gamepad](https://www.protopie.io/learn/docs/connect/gamepad-plugin), [blokdots](https://www.protopie.io/learn/docs/connect/blokdots-plugin), and [Unity](https://www.protopie.io/learn/docs/connect/unity-plugin). 

Additionally, users on the Enterprise plan can upload their own custom plugins, enabling them to connect their prototypes to any hardware, APIs, or apps that support [Socket.IO](http://socket.io/) via ProtoPie Connect.

## Creating Custom Plugins

Custom integrations in ProtoPie Connect can be achieved using Custom Plugins and Bridge Apps. However, we suggest using Custom Plugins instead of Bridge Apps. As Custom Plugin files are portable, they are easier to work with and share among team members.

Hereâs how you create a Custom Plugin:

1. Write your code or reuse an existing [Bridge App](https://github.com/ProtoPie/protopie-connect-bridge-apps).

1. Compile your Bridge App into a single executable binary using [pkg](https://github.com/vercel/pkg)
Index.js files can be compiled for multiple targets (more details [here](https://github.com/vercel/pkg/blob/main/README.md)).

- `pkg -t node16-macos-arm64 index.js` for Mac ARM

- `pkg -t node16-macos-x64 index.js` for Mac Intel

- `pkg -t node16-win-x64 index.js` for Windows

     3.   Copy the executable file to an empty directory and name it `plugin`. Create a metadata.json file and add the pluginâs name `{ "name": "name of the plugin" }`.

     4.  Compress the file (.zip). Your Custom Plugin is now ready to be used!

![compress-custom-plugins](https://cdn.sanity.io/images/vidqzkll/production/4542a01e8d9505d0645b5d373c0b6f05177c5466-2175x1110.png/compress-custom-plugin-connect.png)

5. Import the Custom Plugin into ProtoPie Connect and run it in the terminal.

![protopie-connect-custom-plugin](https://cdn.sanity.io/images/vidqzkll/production/2bac0a0654769ce45243c1e1cb3910a04a669c40-1450x802.png/custom-plugin.png)

You can find some Custom Plugins examples [here](https://github.com/ProtoPie/protopie-connect-custom-plugins).

## What is a Bridge App?

Bridge Apps enable communication between any hardware, APIs, or app supportingÂ [Socket.IO](http://socket.io/) and ProtoPie Connect. Bridge Apps can catch events, receive data from a server, and even work as a single application.

For your convenience, you can use and customize these [Bridge Apps](https://github.com/ProtoPie/protopie-connect-bridge-apps) available on GitHub.

## Connecting Hardware via Bridge App

The main role of a Bridge App is to convert signals from the hardware into Socket.IO messages - a language ProtoPie can understand - and/or vice versa.

1. Connect the Bridge App to ProtoPie Connect.

1. The bridge app converts hardware signals into Socket.IO messages for ProtoPie to interpret. Usually, messages will have the following format:**
**â¦  **{messageId: "HwEventName", value: "ValueAssociatedWithEvent"}** 

1. Prototypes receiving these messages through ProtoPie Connect will respond accordingly. Some hardware supports bidirectional communication, meaning prototypes can send messages to the hardware. This is only possible if the Bridge App can convert Socket.IO messages into signals that the hardware can interpret.

## Connecting to APIs via Bridge Apps

When connecting to APIs via Bridge Apps, the Bridge App converts API responses (e.g., JSON) into individual [Socket.IO](http://socket.io/) messages.

For example, if a prototype needs to retrieve weather data dynamically from an API, the Bridge App would do the following:

1. Convert the JSON response into Socket.IO messages.
â¦  E.g., **{"weather": "sunny", "temperature-celsius": 30.5}**

1. Send Socket.IO messages to ProtoPie Connect that will, in return, relay them to the corresponding prototypes.**
**â¦  **{messageId: "weather", value: "sunny"}**,**
**â¦  **{messageId: "temperature", value: 30.5}**

In the prototype, you need Receive triggers to receive the messages **âweatherâ** and **âtemperature.â** [Learn more](https://www.protopie.io/learn/docs/interactions/triggers#receive) about the Receive trigger.

## Running the Bridge App on the Same Machine

By default, most of these [Bridge Apps](https://github.com/ProtoPie/protopie-connect-bridge-apps) use the IP address **http://localhost:9981** as they assume the Bridge App and ProtoPie Connect run on the same machine.

![running-bridge-app-same-machine](https://cdn.sanity.io/images/vidqzkll/production/0a9c6e8432b7e48b5534718bcd1dd00c7cc170b1-886x298.png/running bridge app same machine.png)

## Running the Bridge App on a Different Machine

If the Bridge App and ProtoPie Connect run on different machines, you can change the IP address to match ProtoPie Connectâs server.

- ProtoPie Connect Desktop: find the server address in the below left corner of the interface.

![ip-address-connect-desktop](https://cdn.sanity.io/images/vidqzkll/production/075172147b91b3ce3ef367dc7e832040e63578fa-1450x128.png/ip-address-connect-desktop.png)

- ProtoPie Connect Embedded: find the server address right after launching in the terminal. 

![ip-address-embedded-systems](https://cdn.sanity.io/images/vidqzkll/production/fdd3c353047ddbdb7aadabe8e8e15fe14f46c225-2232x366.png/ip-address-embedded-systems.png)


---

---
title: "Gamepad Plugin"
url: https://www.protopie.io/learn/docs/connect/gamepad-plugin
---

# Gamepad Plugin

# Using the Gamepad Plugin in ProtoPie Connect

The Gamepad plugin is one of the many built-in plugins in [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started) that allows you to create dynamic, multi-device prototyping experiences. Read along to see how the Gamepad plugin works.

## How It Works

### Prerequisites

In the Security & Privacy Settings of your computer, enable **Input Monitoring** for both ProtoPie Connect and your browser.

![Enable input monitoring.](https://cdn.sanity.io/images/vidqzkll/production/6e166bb1f23aae08718a27a494e8381a44b2936e-2175x1200.png/Gamepad Plugin 2.png)

### Getting Set-Up

1. Open ProtoPie Connect.

2. Connect your Gamepad via USB or Bluetooth to the machine where   ProtoPie Connect is running.

- In the Gamepad Settings window, Device Status will indicate Connected when the Gamepad is detected. If the plugin does not recognize the gamepad, try pressing some buttons on the Gamepad first.

![Connected.](https://cdn.sanity.io/images/vidqzkll/production/e549e2279cc332f36874a06758777cb8f89224d2-1440x900.png/gamepad.png)

3. Press Run to activate the gamepad connection with ProtoPie Connect. 

4. When the Gamepad buttons are pressed, ProtoPie Connect automatically detects the keystrokes and broadcasts message and value pairs to the Pies running on Connect.

## Connecting Multiple Gamepads

ProtoPie Connect supports connections with multiple Gamepads.

- The message will follow the below format:

  - {Gamepad Number}_{Button Name}

- Gamepad Number is assigned from 1 in the following connection order:

  - Gamepad connected first will have Gamepad number of 1.

  - Gamepad connected second will have Gamepad number of 2.

- The number of connected gamepads is displayed in the Gamepad Settings window.

![Gamepad number.](https://cdn.sanity.io/images/vidqzkll/production/1a77cfcfe21140b530e9df0f118c4346a71fb884-2175x1200.png/Gamepad Plugin.png)

## Gamepad Buttons and Messages

Gamepad buttons and messages are as follows (assuming messages are received from the first connected gamepad).

![gamepad buttons](https://cdn.sanity.io/images/vidqzkll/production/8a699ce151a789195f79ff3b7eef3cf7eac73ca1-2000x1675.png/gamepad-plugin-.png)

### Gamepad Plugin â Buttons and Messages

Learn more about ProtoPie Connect's various built-in plugins, such as [API](https://www.protopie.io/learn/docs/connect/api-plugin), [IFTTT](https://www.protopie.io/learn/docs/connect/ifttt-plugin), [Logitech G29 Steering Wheel](https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin), [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin), [blokdots](https://www.protopie.io/learn/docs/connect/blokdots-plugin), and [Unity](https://www.protopie.io/learn/docs/connect/unity-plugin) plugins.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/connect/getting-started
---

# Getting Started

# What is ProtoPie Connect?

[ProtoPie Connect](https://www.protopie.io/connect) is an extension for ProtoPie Studio that allows you to prototype real-world scenarios involving multiple devices, displays, hardware, and APIs seamlessly. It comes with all ProtoPie plans, including the Free plan. Learn more about the [different versions of Connect](https://www.protopie.io/plans) per price tier.

## How to Get Started?

Download and install ProtoPie Connect to start building dynamic prototypes that go beyond traditional mobile interactions:[ Download ProtoPie Connect here.](https://www.protopie.io/connect)

## How Prototypes Communicate in ProtoPie Connect

Communication between multiple devices connected via ProtoPie Connect occurs through Send and Receive messages. The same messaging system is used to pass information back and forth between scenes and components and to create interactions between two devices using ProtoPie Studio as a hub ([connecting devices](https://www.protopie.io/learn/docs/connecting-devices/getting-started)).

Using the [Send response](https://www.protopie.io/learn/docs/interactions/responses#link), you can send messages to prototypes or hardware devices. You need to use the Receive trigger for other prototypes to hear such messages and respond accordingly.

It is important that both Send and Receive are set up to use the same channel in ProtoPie Studio. For prototypes communicating through ProtoPie Connect, the channel must be "**ProtoPie Connect/ Studio.**"

![protopie connect diagram](https://cdn.sanity.io/images/vidqzkll/production/3d90f7a01a70d41074b69cb17b7130799cdb072c-3920x2480.png/send-receive-connect-protopie.png)

## How ProtoPie Connect Works

At its core, ProtoPie Connect acts as a [socket.IO](http://socket.IO) communication server connecting multiple clients:

- ProtoPie prototypes running on smart devices (iOS, Android)

- ProtoPie prototypes running on web browsers on desktops

- Hardware systems (e.g., Arduino, Logitech G29 steering wheel)

- External services (e.g., IFTTT webhooks, public APIs)

The clients can communicate either locally, through a localhost server, or within a local area network (LAN). ProtoPie Connect listens on port 9981 to all the IP addresses of the machine on which it is running. You can also modify the active IP address on ProtoPie Connect by clicking on Network from the menu bar and selecting another IP address.

Let's take automotive as an example. In the following video, tapping a button on the center display triggers animations on the cluster and head-up display (HUD). This is possible thanks to the flexibility and power of ProtoPie Connect.

[Video: ](https://www.youtube.com/watch?v=702pLk1MnqY)

## Connect Desktop vs. Connect Embedded

There are two different types of ProtoPie Connect:

- ***Connect Desktop***

- ***Connect Embedded***

Connect Desktop runs on macOS and Windows. It allows you to run multiple prototypes simultaneously and create immersive multi-screen experiences. It includes built-in plugins to integrate ProtoPie with external hardware devices and services, including Arduino and IFTTT. Enterprise plan users can also upload their own custom plugins to create even more unique digital experiences.

Learn more about [Connect Desktop](https://www.protopie.io/learn/docs/connect/managing-testing-prototypes) and its [API](https://www.protopie.io/learn/docs/connect/api-plugin), [IFTTT](https://www.protopie.io/learn/docs/connect/ifttt-plugin), [G29](https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin), [Arduino](https://www.protopie.io/learn/docs/connect/arduino-plugin), [Gamepad](https://www.protopie.io/learn/docs/connect/gamepad-plugin), [blokdots](https://www.protopie.io/learn/docs/connect/blokdots-plugin), [Unity](https://www.protopie.io/learn/docs/connect/unity-plugin), and [custom](https://www.protopie.io/learn/docs/connect/custom-plugins) plugins. 

As its name suggests, Connect Embedded is designed to run on embedded systems such as Raspberry Pi. Itâs a standalone server application that runs in the terminal. 

Connect Embedded is only available to Enterprise plan users. Learn more about [Connect Embedded.](https://www.protopie.io/learn/docs/connect/connect-embedded) 

## Complete Guide to ProtoPie Connect

![protopie connect free guide](https://cdn.sanity.io/images/vidqzkll/production/9b44362e78be69370302148b5f0a49053dfd30e8-2000x955.png/Frame_3.png)

[ProtoPie School](https://learn.protopie.io/)Â offers aÂ comprehensive guideÂ to ProtoPie Connect in 8 lessons. It starts with a refresher onÂ Send & Receive, then dives into using ProtoPie Connectâs built-in plugins, including how to make yourÂ ownÂ plugins to integrate with just about anything with a screen â and beyond! 
Enroll for freeÂ [here](https://learn.protopie.io/course/protopie-connect).


---

---
title: "IFTTT Plugin"
url: https://www.protopie.io/learn/docs/connect/ifttt-plugin
---

# IFTTT Plugin

# Using IFTTT with ProtoPie Connect

## What is IFTTT?

IFTTT is a web automation service that enables integration with various devices and services including [Twitter](https://ifttt.com/twitter), [Dropbox](https://ifttt.com/dropbox), [Evernote](https://ifttt.com/evernote), [Fitbit](https://ifttt.com/fitbit), [Amazon Alexa](https://ifttt.com/amazon_alexa), andÂ [Google Assistant](https://ifttt.com/google_assistant).

IFTTT stands for 'If This Then That', and the Applets you create in IFTTT work similarly to ProtoPieâs triggers and responses: *If this happens â then that happens.*

Learn more about IFTTT [Applets](https://help.ifttt.com/hc/en-us/articles/4411016949403#Applet).

## How does the IFTTT plugin work?

ProtoPie Connect communicates with IFTTTâs partner services through messages called [Webhooks](https://ifttt.com/maker_webhooks). These work similarly to the Send and Receive messages in ProtoPie. A message (âEventâ) is sent to IFTTT and in response, IFTTT translates the message into an action.

By using ProtoPie Connect with IFTTTâs Webhooks, you can connect your prototypes to all their partner web services and devices.

## Creating Applets in IFTTT

Create an account on the [IFTTT](https://ifttt.com/) website.

### **Configuring the Trigger**

![configuring-trigger-in-ifttt](https://cdn.sanity.io/images/vidqzkll/production/e58bcc7fbae827e5138febf2ae357eb75ee486e0-1345x998.gif/configuring-trigger-ifttt.gif)

1. Once logged in, click on **Create** on the top right corner of the IFTTT page

1. Click on **Add** from the **If This** section and search for **Webhooks**

1. Select â**Receive a web request**â

1. Name your event and click on **Create Trigger**. You can only use letters, numbers, and underscores in the name (for instance: âsend_emailâ)

### Configuring the Action 

![configuring-the-action-in-ifttt](https://cdn.sanity.io/images/vidqzkll/production/40358895da950a8c229133ff5c0449b9989af74a-1345x965.gif/configuring-action-ifttt.gif)

1. Click on the **Add** button in the **Then That** section

1. Search for your desired action in the **Choose a service** field

- For example, âGmailâ - âSend yourself an Emailâ

      3.   Configure the action fields

- Fill in the sections â**Subject, Body, To address, CC address, BCC address, and Attachment URL**â Click on the **Add ingredient** button to add up to 3 customizable values (âValue1, Value2, Value3â) that will have to be configured in ProtoPie Studio (see Configuring Messages in ProtoPie Studio)

- Click on Update Action

- Review your Applet and click on **Finish**

      4.   Your Applet is now active. It can be deactivated and reactivated by switching the **Connected** button.

## Connecting IFTTT to ProtoPie Connect

Configure ProtoPie Connect to send a request to IFTTT.

### Testing your Applet

      1.   Open and log into ProtoPie Connect.

      2.   Select **IFTTT** from the Plugin dropdown menu.

- Copy-paste your private **Webhook Key**, which you can find on the IFTTT website under Explore â âWebhooksâ â Documentation

- Click on the **Run** button

      3.   You can test the Applet in the Test section

- Enter your event name and JSON payload

- Click on **Send**

![testing-your-applet](https://cdn.sanity.io/images/vidqzkll/production/a12a375c72490a11b9e9ff9bdc1a762c12a25c08-4000x1966.png/IFTTT (1).png)

You can verify if your Applet is working correctly by going to My Applets on the IFTTT website and clicking on **View activity**.

![view-activity-applet](https://cdn.sanity.io/images/vidqzkll/production/e1289aafc053a711a7cbecc3efdd22aceec46656-1450x1022.png/ifttt-view-activity-applet.png)

      3.   You will receive an email with the values specified in the JSON payload.

## Configuring Messages in ProtoPie Studio

Now that you have created and tested your Applet, you need to configure the corresponding messages in the prototype using ProtoPie Studio.

Set up the Send responses that will trigger the action in the Applet.

- Use the channel âProtoPie Studioâ to communicate with ProtoPie Connect and activate âSend Value Togetherâ.

- Configure your JSON Payload values if you used one or more in the IFTTT Applet.

![json-upload-ifttt](https://cdn.sanity.io/images/vidqzkll/production/8a88ce4dc739f329525ba9015ac5adf1e9f00aea-1366x660.png/json-payload-protopie-ifttt.png)

- Test the prototype in ProtoPie Connect


---

---
title: "Logitech G29 Steering Wheel Plugin"
url: https://www.protopie.io/learn/docs/connect/logitech-g29-steering-wheel-plugin
---

# Logitech G29 Steering Wheel Plugin

# Using the Logitech G29 Steering Wheel with ProtoPie Connect

Create realistic multi-screen automotive experiences thanks to ProtoPie Connect and the [Logitech G29 Steering Wheel ](https://www.logitechg.com/en-us/products/driving/driving-force-racing-wheel.html)plugin.

[Video: ProtoPie Automotive Solution](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DF2NcgDwJago&feature=youtu.be)

[Learn more](https://www.protopie.io/solutions/automotive) about prototyping with ProtoPie for automotive.

## The Information Flow

The below image illustrates the information flow between ProtoPie and the Logitech G29 steering wheel.

![The information flow between Connect and G29.](https://cdn.sanity.io/images/vidqzkll/production/9859ac65eaf0bd04ce3f42c31bef192079710a5a-2175x1200.png/Connect-steering-wheel-info-flow.png)

- The Logitech G29 steering wheel sends [events and values](https://github.com/nightmode/logitech-g29/blob/HEAD/docs/api.md#events) to ProtoPie Connectâs G29 plugin.

- The G29 plugin converts these events & values to [Socket.IO](http://socket.io) messages for ProtoPie to understand.

- Prototypes added to ProtoPie Connect receive these inputs and respond accordingly using **Send** and **Receive** messages.

## The Ecosystem

Below is a typical ecosystem when using the G29 plugin in ProtoPie Connect.

- 1 machine with USB ports and WiFi/network capabilities

  - To run ProtoPie Connect and connect to the Logitech G29 steering wheel via USB.

- 1 Logitech G29 racing wheel and pedal (optional) set

  - [Example](https://www.amazon.com/Logitech-Dual-motor-Feedback-Responsive-PlayStation/dp/B00Z0UWWYC).

- 2 tablets (iPadOS or Android) or 2 computer monitors

  - For prototypes that need to be opened on a larger display (ProtoPie Connectâs web browser, ProtoPie Player on tablets).

- 1 smartphone (iOS or Android)

  - For prototypes that need to be opened on a mobile display (ProtoPie Player).

## Getting Set Up

Below is the most recommended setup for handling messages between the Logitech G29 steering wheel and prototypes made in ProtoPie. At the end your setup should look like the one shown in the video at the top of this page.

![Connect and G29 - the setup.](https://cdn.sanity.io/images/vidqzkll/production/7980a5b3e44427598c981c1b43c36bf362d30eb0-2175x1200.png/Connect-steering-wheel-setup.png)

- Use 2 **large displays** and 1 **smartphone** for running your prototypes (smartphones, tablets, and monitors can all serve as displays).

- Connect **ProtoPie Player** to **ProtoPie** **Connect** via WiFi (same LAN).

- Connect the **Logitech G29** steering wheel via USB to the machine where **ProtoPie** **Connect** is running:

  - In ProtoPie Connect click on the **Plugins** button in the upper right corner.

  - Select **G29** in the Plugin list.

![The G29 plugin in ProtoPie Connect.](https://cdn.sanity.io/images/vidqzkll/production/92197db76bb519e3f93968b5dc1e0b58a5223b3b-1450x800.png/G29.png)

  - If you have the PlayStation version of the G29, it has a switch that allows you to toggle between PS3 and PS4 compatibility mode. Make sure it is switched to **PS3 mode.**

![PS3 mode in G29 steering wheel.](https://cdn.sanity.io/images/vidqzkll/production/5b168b66db75d0378ca0f5b89f3d8ea4663a18ed-2175x1200.png/Connect-G29-PS3-mode.png)

  - **Plug in** the **G29** USB cord into the computer.

  - Click on the **Run** button.

![Run the G29 plugin in ProtoPie Connect.](https://cdn.sanity.io/images/vidqzkll/production/be974fc2861efbca400ef6e2962f397a49523567-1450x810.png/G29-1.png)

  - The G29 steering wheel is now ready for use.

![G29 plugin is now ready to use.](https://cdn.sanity.io/images/vidqzkll/production/0eef53caf4be79867ff4e444d0afcad992656633-1450x809.png/G29-2.png)

## Examples

### Turning the Steering Wheel Left

Turn the steering wheel left to rotate and change the color of a layer in ProtoPie Studio.

![Turning the Steering Wheel Left.](https://cdn.sanity.io/images/vidqzkll/production/cf3c555274e1aa9ef43258ad588c893b7fdffe06-2175x1200.png/Connect-steering-wheel-left.png)

- When you turn the Logitech G29 steering wheel fully to the left, the G29 plugin converts the incoming event into a message ProtoPie can interpret.

- The prototype loaded to ProtoPie Connect receives this message and assigns it to a variable when triggering the Color and Rotate responses.

### Pressing a Button on the Steering Wheel

Press the triangle button on the steering wheel to trigger actions in two separate prototypes.

![Pressing a Button on the Steering Wheel.](https://cdn.sanity.io/images/vidqzkll/production/155ddbf57bbed9732a202a63c66c4204c8703e7c-2175x1200.png/Connect-steering-wheels-button.png)

- When you press the triangle button on the Logitech G29 steering wheel, the G29 plugin converts the incoming event into a message ProtoPie can interpret.

- The two prototypes loaded to ProtoPie Connect respond to this message accordingly, depending on how you set up your interactions.

  - For example, one prototype recreates a blinking light and the other prototype shows a text saying âEmergencyâ.


---

---
title: "Testing Prototypes"
url: https://www.protopie.io/learn/docs/connect/managing-testing-prototypes
---

# Testing Prototypes

# Testing Prototypes in ProtoPie Connect 

 ProtoPie Connect allows you to test your prototypes on a variety of smart devices and desktop browsers. You can use ProtoPie Connect in the following ways:

- To test prototypes using ProtoPie Connect and ProtoPie Player

- To test prototypes using ProtoPie Connect and ProtoPie Player for Wear OS

- To test prototypes on web browsers

- To test prototypes in [Stage View](https://www.protopie.io/learn/docs/connect/custom-layer-integrations#creating-a-stage-view).

Download ProtoPie Connect [here](https://www.protopie.io/download).

## Adding Prototypes to ProtoPie Connect

Before testing, load your prototypes into ProtoPie Connect by following these simple steps:

- Click the + New button and select the prototypes you want to add. Or drag-and-drop prototypes into ProtoPie Connect's interface.

  - Enterprise users can open prototypes directly from ProtoPie Cloud by selecting Cloud Pie. To fetch the most recent version of a Cloud Pie, click on the circular arrow icon (Reload).

- Select the Pie file and click the trash icon to remove a prototype from the list.

- To replace a prototype, place the cursor on the prototype and click on the two-way arrow icon.

  - Technical note: Adding a new Pie file creates a new ***pieid***. Replacing a Pie file reuses the same pieId of the previous prototype. 

![managing prototypes](https://cdn.sanity.io/images/vidqzkll/production/50a8cf5a6892a40645c7ab6091e76cea313f3dc0-1316x856.gif/import-new-pie-connect.gif)

### Arranging Pies into Groups 

To keep your Pies organized and easy to manage, you can group them together. To create a new **Pie group**, click on the Group icon. To add a Pie to a group, drag and drop it into the group. Be sure to expand the group before doing so.

- To move a Pie from one group to another one, drag and drop it into another group.

- Only groups containing at least one Pie can be expanded/ collapsed.

- Only groups containing at least one Pie can be selected/ deselected.

- To rename a group, double-click on the group name and enter the new name.

- To delete a group, hover over it with the cursor and click the Trash icon.

![users can now group their pies in Protopie connect with the Group feature](https://cdn.sanity.io/images/vidqzkll/production/980ad01bf0ab651f6bb4a251dc6c473a4b44a2a2-1314x858.gif/Pie-groups-connect.gif)

## Testing Prototypes Using ProtoPie Connect & ProtoPie Player

[ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) is a free companion app for ProtoPie Studio and ProtoPie Connect. You can view, experience, and test any prototypes added to ProtoPie Connect on iOS, iPadOS, and Android devices. 

There are three ways to connect ProtoPie Player to ProtoPie Connect:

1. Scanning the QR code

1. Entering the IP address

1. Using a USB cable  

### Connect ProtoPie Player to ProtoPie Connect Scanning the QR Code

1. Ensure your computer and smart device are connected to the same WiFi network.

1. Click on Connect for the prototype you want to open in ProtoPie Connect.

1. Select ***QR Code*** from the list.

1. Tap on theÂ Scan QR CodeÂ button in ProtoPie Player.

1. Scan the QR code to run the prototype in the Player.

![scan qr code player connect](https://cdn.sanity.io/images/vidqzkll/production/e3dbf19b1d56b9f9d3a4b2429599566384f2780c-1450x800.png/1-Connect-managing.png)

### Connect ProtoPie Player to ProtoPie Connect Entering the IP Address

1. Make sure your computer and smart device are connected to the same WiFi network.

1. Tap onÂ Type IP AddressÂ from the dropdown menu in ProtoPie Player.

1. Enter the IP address shown in ProtoPie Connect. 

1. Tap on the Connect button to run the prototype on your smart device.

![entering ip address connect](https://cdn.sanity.io/images/vidqzkll/production/9d1ff670e4977f89dfe1a23f1daf5fe95dfe6095-1450x800.png/2-Connect-managing.png)

## Testing Prototypes Using ProtoPie Connect & ProtoPie Player for Wear OS

[ProtoPie Player for Wear OS](https://www.protopie.io/learn/docs/player/player-for-wear-os), unlike the regular ProtoPie Player, only works in conjunction with Connect Enterprise. 

1. Make sure both ProtoPie Player for Wear OS and ProtoPie Connect are connected to the same internet network.

1. Open themâProtoPie Player for Wear OS and ProtoPie Connect will automatically detect each other 

1. Click on Tap to connect in the ProtoPie Player for Wear OS to pair it with ProtoPie Connect.

1. Add a smartwatch prototype to ProtoPie Connect.

1. Click on the Run button at the top of ProtoPie Connect's interface to open the prototype in the Player for Wear OS.

1. To restart or exit the prototype, double-tap the smartwatch screen. 

## Testing Prototypes on Web Browsers

To view a prototype on a browser, it is recommended to use a Chromium browser for optimal performance. There are two ways to open a prototype on a desktop web browser from ProtoPie Connect. 

- On the same machine where ProtoPie Connect is running 

- On a different machine 

### Testing Prototypes On the Same Machine

1. Click on the Web Browser icon next to the prototype you want to open.

1. In the browser, the URL will have the following format: http://localhost:9981/.

![ProtoPie Connect IP address ](https://cdn.sanity.io/images/vidqzkll/production/cd974abbca5dade134c7f187e6b24446bcfcaef3-1450x800.png/3-Connect-managing.png)

### Testing Prototypes On a Different Machine

1. Ensure your computer and the other machine are connected to the same WiFi network with ProtoPie Connect.

1. Open any web browser on the other machine.

1. Enter your ProtoPie Connect IP address in the address bar. The ProtoPie Connect interface will be displayed.

1. Click on the Web Browser icon next to the prototype you want to open.

1. In the browser, the URL will have the following format: http://protopie.connect.ip.address:9981/.

### Using Voice Prototyping Features in the Web Browser

Starting from ProtoPie Connect 1.8.0, voice prototyping features are supported in the Web Player, just like they are in the ProtoPie Player app for iOS/Android and ProtoPie Studio's Preview window. Currently, the supported features are:

- [Voice Command Trigger](https://www.protopie.io/learn/docs/voice-prototyping/voice-command-trigger)

- [Speak Response](https://www.protopie.io/learn/docs/voice-prototyping/speak-response)

- [Listen Response](https://www.protopie.io/learn/docs/voice-prototyping/listen-response)

#### Compatible web browsers

Each browser behaves differently when dealing with microphone permissions. To use the Voice Command Trigger and Listen Response, the browser needs microphone permission from the user. The browser will ask for **microphone permission** when the microphone needs to be enabled in the prototype, like in the screenshot below. To enable microphone access, click Allow.

![Enabling microphone access](https://cdn.sanity.io/images/vidqzkll/production/4bd9f730ca9d37a41b217ca6f8ab5169799ac329-2175x1200.png/ProtoPie Connect - enable mic.png)

Voice prototyping features for the ProtoPie Connectâs Web Player work best in Chromium browsers such as **Google Chrome** and **Microsoft Edge**. To properly play voice interactions some setup may be required on the browser side depending on the browser used and how the prototype is loaded.

#### Web Browser Setup

There are two ways to play prototypes in the web browser:

1. On IP address

1. On http://localhost:9981/

Playing prototypes on http://localhost:9981/ requires no setup and works across browsers.

Playing prototypes on IP address (e.g., http://192.168.0.40:9981/) requires a **one-time browser setup** to enable microphone usage, and is supported on **Google Chrome** and **Microsoft Edge**.

Chromium browsers will only allow your device's microphone permission when a site has a secure origin â i.e. serve from https or localhost.

The following one-time setup is required to use a microphone with ProtoPie Connect's Web Player.

1. In the Chrome/Edge browser, navigate to `flags`.

`chrome://flags/#unsafely-treat-insecure-origin-as-secure`

`edge://flags/#unsafely-treat-insecure-origin-as-secure `

2. Enable `Insecure origins treated as secure`.

![Adding the ProtoPie Connect server details.](https://cdn.sanity.io/images/vidqzkll/production/cc621829db8308280082ec0de1995857686b21d2-2175x1200.png/ProtoPie Connect - one time browser set up.png)

3. Add the ProtoPie Connect server address with port number 9981.

Note: The server address can be found in the bottom left corner of ProtoPie Connect.

![ProtoPie Connect server address](https://cdn.sanity.io/images/vidqzkll/production/9d1ff670e4977f89dfe1a23f1daf5fe95dfe6095-1450x800.png/2-Connect-managing.png)

4. Relaunch (Restart) the Chrome/Edge browser.

![Relaunch Google Chrome.](https://cdn.sanity.io/images/vidqzkll/production/a789cbf5c1d64f5792117bb008a4adb3f1c4d078-2175x1200.png/ProtoPie Connect - relaunch chrome.png)

### Customizing View Options

As on [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#managing-display-options), you can customize how prototypes display on the web browser using **URL parameters.**

- URLs with such parameters have the following format: http://localhost:9981/pie?pieid=[ number]&name=[pie name]â¦

- Use the â**&â** symbol to separate parameters in the URL.

- If you use a browser on a different machine, replace **localhost** with the IP address shown in ProtoPie Connect. For example, http://192.168.123.101:9981/pie?pieid=23.

**Some examples of URLs with parameters:**

- Change the background color to white, show hotspot hints, and scale the prototype to fit the screen.

  - **http://localhost:9981/pie?pieid=1&bg=white&touchHint=true&scaleToFit=true**

- Change the background color to yellow, and hide the cursor

  - **http://localhost:9981/pie?pieid=1&bg=yellow&cursorHide=true**

## FAQs


---

---
title: "Feature Comparison"
url: https://www.protopie.io/learn/docs/connect/protopie-connect-pro-vs-enterprise
---

# Feature Comparison

# ProtoPie Connect Feature Comparison

**ProtoPie Connect** is available for all plans and comes in three tiers: **Connect Free**, **Connect Core**,** **and** Connect Enterprise**.

- **Free Plan** users have access to **Connect Free**, which includes essential features to get started.

- [**Basic Plan**](https://www.protopie.io/plans/basic) and [**Pro Plan**](https://www.protopie.io/plans/pro) users can upgrade their experience by **adding Connect Core**.

- [**Enterprise Plan**](https://www.protopie.io/plans/enterprise) users get **Connect Enterprise** included as part of their plan, offering the most advanced capabilities.

Below is a feature comparison table that highlights the differences between the different versions of Connect. For a more detailed feature breakdown, [check out our pricing page](https://www.protopie.io/plans).


---

---
title: "Unity Plugin"
url: https://www.protopie.io/learn/docs/connect/unity-plugin
---

# Unity Plugin

# Unity Plugin

The Unity plugin is free for anyone to download and install. When integrating with ProtoPie Connect, Connect Core Add-on users can display up to one Unity layer. However, full message-based interactivityâsuch as animating Unity models or passing valuesâalong with support for unlimited layers, is exclusively available with Connect Enterprise.


![Plan Feature Availability](https://cdn.sanity.io/images/vidqzkll/production/6ccf21b86d29c8321802042da394a95f9da81a86-1780x730.png/Asset #1 (4).png)

 

Click here to [download the ProtoPie Connect Unity plugin](https://www.notion.so/protopie/ProtoPie-Plugin-for-Unity-14d4029732554ac1830c56c6a92eada1).

## **Workflow for Integrating Unity with ProtoPie**

To prototype integrated interactions between ProtoPie and Unity, we suggest the following workflow:

1. Define the message set (mapping table) to be used for communicating with Unity. The Pies will interact with Unity via messages using Send/Receive features.

- In ProtoPie, messages in the Send response trigger events in Unity. When Unity sends a message to ProtoPie, messages in the Receive trigger serve as the identifier for the appropriate responses in ProtoPie.

2. [Install the Unity plugin](https://www.notion.so/protopie/ProtoPie-Plugin-for-Unity-14d4029732554ac1830c56c6a92eada1) for the Unity project.

3. Define the mapping between ProtoPie messages and Unity events.

4. When ready to test together, [export the Unity scene as a WebGL build](https://www.protopie.io/learn/docs/connect/custom-layer-integrations#configuring-unity-layers) and add the build files as source files to the Unity layer in ProtoPie Connect.

5. Arrange the ProtoPie and Unity layers according to the desired layout and test the interactions together on the [Stage View](https://www.protopie.io/learn/docs/connect/custom-layer-integrations) in ProtoPie Connect.

## Unity Plugin Overview

- The plugin is installed in the Unity project as a package and allows one to map ProtoPie messages with Unity events without having to write any code. The plugin can be added to existing Unity projects in an unobtrusive manner and doesnât interfere with or break any existing Unity components.

- The plugin works by creating a **ProtoPie object** inside the Unity scene and utilizing the script component **Message Interaction** (provided by the package). The ProtoPie object is responsible for mapping the ProtoPie messages with events in Unity. Because the ProtoPie object handles all the mapping between the two platforms, there is no need to customize the Unity code elsewhere to make this integration happen.

- In the **Message Interaction** script component, one assigns a mapping table to use with the Unity scene. The mapping table is a list of messages to be used between ProtoPie and Unity. Once a mapping table has been assigned, the user can add the **Event(Unity)-Message(ProtoPie) Mappings** to be used in the Unity scene.

- In the **Event(Unity)-Message(ProtoPie) Mappings**, the user can designate the message mapping to use in the scene, the message direction, the desired action in Unity, the values to send back to ProtoPie, etc.

## **Unity Plugin Installation and Setup**

1. In the Unity Project, [install the ](https://www.protopie.io/14d4029732554ac1830c56c6a92eada1?pvs=25)[ProtoPie Unity](https://www.protopie.io/14d4029732554ac1830c56c6a92eada1?pvs=25)[ plugin](https://www.notion.so/protopie/ProtoPie-Plugin-for-Unity-14d4029732554ac1830c56c6a92eada1).

2. In the Unity scene, create an empty object and name it "**ProtoPie**".

- The name must be "**ProtoPie**" (case sensitive) because ProtoPie Connect detects the object for message interactions using that name

3. Add âMessageInteraction.csâ (from ProtoPie Unity Package) script component to the **ProtoPie object**.

4. Select Add Component â Scripts â ProtoPie.Interaction â Message Interaction.

![Select Add Component â Scripts â ProtoPie.Interaction â Message Interaction](https://cdn.sanity.io/images/vidqzkll/production/4f4bb7b826e25df929121a0c978c51bd606551f1-1440x900.png/connect-msg.png)

4. Add **MappingTable** to the **Message Data** field in the Message Interaction component.

![Add MappingTable to the Message Data field in the Message Interaction component. ](https://cdn.sanity.io/images/vidqzkll/production/bc61936b5bdacd5fafde55818d02cf8a3ed9e76a-2000x2153.png/Screenshot_2024-05-07_at_1.00.34_PM.png)

- The MappingTable, in essence, defines the message set to be communicated between ProtoPie and Unity.

- It is a configuration file in YAML format, which allows you to specify the labels, the message to be transmitted, and the message flow direction.

- The mapping table is located in the package folder named MappingTablet.asset. Here, you can add/remove/edit the entries in the message mapping list.

5. The Unity scene is now ready to be used with ProtoPie Connect. Add your first mapping by pressing the **Add Mapping** button under Event(Unity)-Message(ProtoPie) Mappings.

## Message Mapping in the Unity Plugin

![message mapping](https://cdn.sanity.io/images/vidqzkll/production/c17311d578070519de8853f8b1fa6a142fe3d667-2000x2762.png/Screenshot_2024-05-07_at_1.09.09_PM.png)

ProtoPie and Unity layers communicate via messages to add interactivity between them. 

To add a message mapping, select **Add Mapping** to define which mapping to utilize. For each mapping, you will be able to select one of the mappingsÂ defined in the mapping table (the one used in the Message Data field).

### Attribute Definitions

- **Mapping Label**: the label or index of the mapping defined in the mapping table.

- **Message**: The message (or messageID in [socket.IO](http://socket.IO) terms) to send/receive between ProtoPie and Unity. This will correspond to the message in ProtoPieâs Send Response and Receive Trigger.

- **Message Direction:** The direction of message communication (ProtoPie to Unity, Unity to ProtoPie, Both Ways, None).

- **Desired Action (String)**: The action (method/function) that should be executed in Unity when ProtoPie sends the corresponding message to Unity (Applicable only when Message Direction is ProtoPie to Unity and Both Ways).

![message mapping](https://cdn.sanity.io/images/vidqzkll/production/daa5d3e85481a18b46441712e01fbb1d162aadb5-2000x1882.png/better.png)

  - The user should select the source object and the method to execute the action.

  - If ProtoPie sends a value along with the message, that value can be passed along as a String parameter to the action (method/function)

  - Note: The 'addCube(string)' option under 'Static Parameters' is not configurable at runtime. Instead, the string value must be predefined within the Unity Editor prior to building the project.

- **Event Object & Event to trigger message**: The Unity object and event that would trigger Unity to send the message to ProtoPie (Application only when Message Direction is Unity to ProtoPie and Both Ways).

- **Value Source Object & Value to Send:** (Optional) When sending a message from Unity to ProtoPie, additional data can be sent to ProtoPie via the messageâs value. The **Value Source Object** and **Value to Send** attributes define what kind of data to send back to ProtoPie.

  - Note: The plugin will recognize public string variables attached to the source object.


---

---
title: "Connecting blokdots"
url: https://www.protopie.io/learn/docs/connecting-devices/blokdots
---

# Connecting blokdots

# blokdots & ProtoPie

[blokdots](https://blokdots.com/) is a code-free software used to build interactive hardware prototypes with [Arduino](https://www.protopie.io/learn/docs/connect/arduino-with-connect). By using [ProtoPie](https://www.protopie.io) and blokdots together, you can bridge the gap between hardware and software prototyping without a line of code.

This integration is available with all plans. However, by using blokdots with [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started) you can unlock new possibilities, such as the ability to create hardware-software interactions involving three or more devices. Learn more about how the [blokdots plugin works](https://www.protopie.io/learn/docs/connect/blokdots-plugin) in ProtoPie Connect. 

Here is the simplest ecosystem for connecting ProtoPie to blokdots:

- ProtoPie Studio - for creating interactions.

- [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) - for running prototypes on smart devices.

- blokdots - to facilitate the communication between Arduino and prototypes via [socket.IO](http://socket.io/). 

![blokdots_and_protopie_environment](https://cdn.sanity.io/images/vidqzkll/production/e6281a443275cb3fd116a17ca4081b7dbb04e22d-2984x1172.png/blokdots_and_protopie_environment.png)

## Getting Ready

To use blokdots with ProtoPie you will need the following:

- Have the [blokdots app](https://blokdots.com/) installed on your desktop.

- Set up your Arduino board. Check the supported boards [here](https://blokdots.com/documentation/#Supported-Boards).

- A USB cable to connect your Arduino board to your laptop or PC.




- Activate the free trial of blokdots pro.

## Connecting Arduino to blokdots

Open blokdots and connect your Arduino board to your laptop or PC. 

Once you see that your board is ready in the top-left corner, you can start setting up your components.

### Setting Up Components in blokdots

1. Click  **Connect A New Component** and pick the ones you want to connect.

1. Choose an available Grove slot or hardware pin from the list

1. Click on **Set Component.**

This step is necessary for blokdots to know which components of the Arduino board to control.

![blokdots wizard bg](https://cdn.sanity.io/images/vidqzkll/production/091b7da8514db455c765eeab447293683e4328ab-2248x1696.png/blokdots-wizard-bg.png)

       

## Connecting ProtoPie with Arduino via blokdots

The blokdots app allows ProtoPie and Arduino to send messages from one to another. To make this happen, you will need to:

1. **Set up Send and Receive in ProtoPie Studio**

In ProtoPie Studio, the [**Receive Trigger**](https://www.protopie.io/learn/docs/interactions/triggers#receive) and the [**Send Response**](https://www.protopie.io/learn/docs/interactions/responses#send) will initiate communication between the devices. Make sure to set the **Channel** to **ProtoPie Studio.** The **Message** and **Value** can be set to whatever you wish.

**      **2.**   Create condition cards in blokdots**

To add logic to a blokdots component, you need to add and configure cards in the main area of the Project View. There are two types of cards in blokdots: âIf This Then Thatâ cards and âMappingâ cards.

As the final interactions take place between **ProtoPie Player** and **Arduino,** the combination of both will make communication possible.

### Receiving messages from blokdots to ProtoPie

To send a message from blokdots to ProtoPie, a condition card should have the following structure:

- If `the action of any input hardware component`

- Then `ProtoPie Player` should `send`Â `message`

In the smart home prototype example below, turning the Potentiometer on the Arduino board will change the temperature degree value displayed on the pie file running in the ProtoPie Player.

![blokdots to protopie](https://cdn.sanity.io/images/vidqzkll/production/d0195bc31ad8bb1db4d9685b5d61d4b907147b0d-1188x262.png/blokdots-to-protopie.png)

To receive messages from blokdots, use the **Receive** trigger in ProtoPie Studio as below.

![receive_trigger_protopie_studio](https://cdn.sanity.io/images/vidqzkll/production/4fef2678c0e1f920bd7804cabfbb0414bbe7313e-1760x953.png/receive_trigger_protopie_studio.png)

### **Sending messages from ProtoPie to blokdots**

To send messages from ProtoPie Studio to blokdots, use the **Send** response.

![send_response_protopie_studio](https://cdn.sanity.io/images/vidqzkll/production/c4c280987357b6a60faae371988bf02a7124ea2f-1760x952.png/send_response_protopie_studio.png)

To receive a message from ProtoPie, the condition card in blokdots should have the following structure:

- If `ProtoPie Player` is `receiving`Â `message`

- Then `the action of any input hardware component`

![protopie to blokdots](https://cdn.sanity.io/images/vidqzkll/production/397453f25df630ca995f48fdb0ccef9f8be012ca-1192x266.png/protopie-to-blokdots.png)

## Testing your Interactions

To test your interactions, do the following:

  1.    Connect ProtoPie Player with blokdots (iOS only for now)

Scan the QR code that blokdots will show when hovering above the ProtoPie icon in the lower-left cornerÂ or type the IP address. The ProtoPie Player component will change to green once it is set up.

![connecting_player_with_blokdots](https://cdn.sanity.io/images/vidqzkll/production/86e224f171452ed5458f8fa8e46185be7af031ea-725x400.png/connect-blokdots-player.png)

 2.  Connect ProtoPie Studio with ProtoPie Player

[Learn more](https://www.protopie.io/learn/docs/player/getting-started) about how to connect ProtoPie Player.

3.   Run your project in blokdots

Click on the **Run Project** button** **at the top of the project window.** **

![run blokdots project](https://cdn.sanity.io/images/vidqzkll/production/4202f5b40ffbabef84d5f07340c14408b9ac3e74-1072x712.png/run-blokdots-project.png)

If you want to learn more about the ProtoPie and blokdots integration and test it out on your own, check out this step-by-step [tutorial.](https://www.protopie.io/blog/protopie-and-blokdots-no-code-arduino-prototyping) 

## FAQs


---

---
title: "Connecting Mobile Devices"
url: https://www.protopie.io/learn/docs/connecting-devices/connecting-mobile-devices
---

# Connecting Mobile Devices

# Connecting Mobile Devices

In addition to designing interactions on a single device, ProtoPie enables prototyping interactions involving multiple devices communicating with each other. For example, you can easily simulate a chat or money transfer experience between connected devices.

[Video: Money Transfer - Video](https://www.youtube.com/watch?v=8HFkT2PsOQc)


There are two ways of creating connected experiences in ProtoPie:

- using ProtoPie Studio as a hub

- using ProtoPie Connect

You can connect two prototypes using [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem#proto-pie-studio) as a hub. This feature is available with all plans. ProtoPie Studio must remain open while testing interactions using this method.

You have two options for connecting prototypes via ProtoPie Studio:

1. You can connect two prototypes running in [the Player app](https://www.protopie.io/learn/docs/player/getting-started). Ensure that both devices and the computer running ProtoPie Studio are connected to the same network.

1. You can connect a prototype in ProtoPie Studio with another prototype running in the Player app. Both ProtoPie Studio and the Player app should be connected to the same network.

Alternatively, you can connect your smart devices to a computer via USB. This method eliminates the dependency on the network connection.

[Learn more](https://www.protopie.io/learn/docs/player/getting-started)Â about connecting smart devices to ProtoPie Studio.

If you are subscribed to a Pro or Enterprise plan, you can create a wider array of connected experiences using [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

## Getting Started

To enable cross-device interactions, ProtoPie utilizes [Send responses](https://www.protopie.io/learn/docs/interactions/responses#send) and [Receive triggers](https://www.protopie.io/learn/docs/interactions/triggers#receive-trigger-properties). A response is triggered when a device with the Receive trigger accepts a message sent from another device using a Send response. It is essential for the received message on one device to match the message sent from the other device.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DZxgxlLiEelQ)

### Setting up the Send Response

### Setting up the Receive Trigger

### Example

![bridge ex](https://cdn.sanity.io/images/vidqzkll/production/b00f588a19d492bdb17821f494cb11a931438fd9-1076x540.gif/bridge_ex.gif)


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/enterprise/getting-started
---

# Getting Started

# ProtoPie Enterprise

ProtoPie Enterprise provides a secure and scalable solution to foster collaboration across your entire organization. 

With exclusive features, plus [enhanced security](https://www.protopie.io/learn/docs/security/overview) and dedicated support, ProtoPie Enterprise empowers your organization to drive seamless collaboration with multiple team spaces within a single ProtoPie environment.

Service admins play a crucial role in configuring and overseeing ProtoPie Enterprise environments. Discover more about the [service admin privileges](https://www.protopie.io/learn/docs/enterprise/service-admin) in the Enterprise plan.

## ProtoPie Enterprise Environment

ProtoPie Enterprise is available in two tiers:

- **On-Premises**: Utilize your organization's own server and physical hardware for complete control and privacy.

- **Private Cloud**: Enjoy the security and reliability of an AWS-enabled dedicated space exclusively for your organization.

## Creating an Account

Enterprise team spaces are separate from regular ProtoPie spaces and require a dedicated account. However, itâs possible to activate an Enterprise access alongside your existing Free or Pro plan access. 

### Signing Up for ProtoPie Enterprise

 New members who are invited to join an Enterprise environment by a service admin or a team owner/admin will receive an invitation email with a unique link. Just click on the link to create your ProtoPie enterprise account.

If you need guidance on the specific Enterprise URL to use for logging in, your service admin can assist you.

### Logging into ProtoPie Studio

![Logging into studio](https://cdn.sanity.io/images/vidqzkll/production/4510c79c29c6d666243e54f5a3b3224d04645002-1440x872.gif/enterprise login.gif)

1. Open ProtoPie Studio.

1. In the welcome window, click on "Log in for Enterprise".

1. Enter the enterprise URL provided by the service admin.

1. Click on "Connect."

1. In the login window, enter your enterprise accountâs credentials.

1. Click on "Open ProtoPie" in the pop-up window.

1. Wait a few seconds as you are redirected to ProtoPie Studio.

Important notes:

- The Enterprise URL is unique to your organization's ProtoPie Enterprise environment.

- Enterprise areas are separate from regular personal spaces (Pro and Free plans). To log into ProtoPie Enterprise, you need to create an account specifically for your Enterprise environment.

New to ProtoPie?Â [Learn more](https://www.protopie.io/learn/docs/getting-started)Â about getting started with ProtoPie.

## Member Types & Roles

In addition to team owner, team admin, editor, and viewer, ProtoPie Enterprise environments include one more type of member: the service admin.

Learn moreÂ about [member types](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin) & [roles](https://www.protopie.io/learn/docs/teams/editors-and-viewers).

### Service Admin

The service admin holds a crucial role in overseeing the entire ProtoPie Enterprise environment. They have administrative privileges and are responsible for managing members, teams, and authentication. 

If you encounter any issues with your account or team, you can reach out to the service admin within your company for assistance.

Discover more about the [service admin privileges](https://www.protopie.io/learn/docs/enterprise/service-admin) in the Enterprise plan.


---

---
title: "Organization Settings"
url: https://www.protopie.io/learn/docs/enterprise/organization-settings
---

# Organization Settings

# Organization Settings

Service admins can easily manage their ProtoPie Enterprise environment by accessing the **Organization settings** section. This portal can be easily opened from the home page of each Enterprise environment in [ProtoPie Cloud](https://cloud.protopie.io/).

Learn more about the [Service admin](https://www.protopie.io/learn/docs/enterprise/service-admin) role in Enterprise plans.

![Managing ProtoPie Enterprise Organization Settings](https://cdn.sanity.io/images/vidqzkll/production/e99a5bd2745a0602b662d301edb022d982e7deeb-1879x1550.png/organization_settings.png)

These are the key settings and features available in Organization settings:

1. [**Teams**](https://www.protopie.io/learn/docs/enterprise/organization-settings#managing-teams-in-organization-settings): Efficiently manage and organize your team settings. In this section, you can create teams, designate team owners and admins, and adjust team settings to optimize collaboration within your organization.

1. [**Members**](https://www.protopie.io/learn/docs/enterprise/organization-settings#managing-members-in-organization-settings): Add new members to your Enterprise environment, assign roles and permissions to them, and remove them when necessary. This section lets you control access and ensure the right individuals are part of your ProtoPie Enterprise team.

1. [**Organization Fonts**](https://www.protopie.io/learn/docs/enterprise/organization-settings#managing-fonts-in-organization-settings): Enhance your prototypes by uploading custom fonts. This feature ensures that your team's custom fonts are consistently displayed across ProtoPie Studio, Connect, Cloud, and Player. All editors will have access to these custom fonts, maintaining brand consistency throughout your designs.

1. [**Security**](https://www.protopie.io/learn/docs/enterprise/organization-settings#managing-security-in-organization-settings): Customize and configure your Enterprise environment's security settings. Here, you can implement measures such as restricting external sharing of your pie files, setting session durations, and managing accounts. By adjusting these settings, you can strengthen the security of your organization's data and ensure compliance with your specific requirements.

1. [**Authentication**](https://www.protopie.io/learn/docs/enterprise/organization-settings#managing-authentication-in-organization-settings): Manage how members sign up and log in to ProtoPie Enterprise using email & password or Single sign-on (SSO).

1. [**Report**](https://www.protopie.io/learn/docs/enterprise/organization-settings#accessing-reports-in-organization-settings): Export member data in CSV format. The report contains details about the members' accounts, such as their email addresses and roles. It also provides information about their activity, including the date they created their account, their last login date, and the date they were invited.

1. [**General Information**](https://www.protopie.io/learn/docs/enterprise/organization-settings#managing-the-general-information-of-your-organization): Access the General Information tab to view essential details about your ProtoPie Enterprise environment. This includes information such as your environment's name, plan expiration date, version number, and contact details for the service administrator. This overview provides a quick reference for key information related to your ProtoPie setup.

## Managing Teams in Organization Settings

With ProtoPie Enterprise, you can create and manage multiple teams within a single environment. In Organization settings, navigate to the **Teams** section to access an overview of all the teams in your ProtoPie Enterprise environment.

Within this section, you can easily gather essential information about each team, including the team's name, respective owners, and the number of members in each team.

![Manage ProtoPie Enterprise Teams ](https://cdn.sanity.io/images/vidqzkll/production/eff396475a67605b9a85892577c4b31c3a68355a-817x411.png/teams.png)

### Creating New Teams

Follow these steps to create a new team in your enterprise environment:

1. In Teams, click on **Create New Team**.

1. Fill in the team name.

1. Assign a member as the team owner.

![Creating teams in ProtoPie Enterprise](https://cdn.sanity.io/images/vidqzkll/production/9ae464830b49ba80daef76bc653506c1a072b8d1-876x714.png/create-team.png)

### Team Information

For more details about a specific team,  click on the respective team name from the list. You will find an overview of its composition and settings. This includes information on the number of editors and viewers associated with the team and their corresponding status (active or pending).

Moreover, you can delete teams and adjust team members' roles as needed, ensuring the right level of access and privileges.

While each team has a single owner, they can also have one or more team admins to assist in managing team activities and settings. [Learn more](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin) about team owners and team admins.

![Information section of ProtoPie Enterprise teams ](https://cdn.sanity.io/images/vidqzkll/production/ce7cfe7844ebd2654e9acfb532769ab1645d6639-1122x703.png/protopie-team.png)

## Managing Members in Organization Settings

In **Organization settings**, under **Members**, find an overview of how many editors and viewers joined your ProtoPie Enterprise environment. Also, see how many editor seats are taken and how many are still available.

![Managing Members in ProtoPie Enterprise plans ](https://cdn.sanity.io/images/vidqzkll/production/c67ae992df629f1e78e7a988f61886f806a31718-1080x781.png/members.png)

Here, you can manage all the members (regardless of their teams). You can verify their status (active, deactivated, or pending) and roles.

There are two roles: editor and viewer.Â [Learn more](https://www.protopie.io/learn/docs/teams/editors-and-viewers)Â about editors and viewers.

### Inviting New Members

1. Click on Invite **New Member**.

1. Enter the email address(es) of the people you'd like to invite and select Invite. 

1. They will receive an email with an invitation link.

1. They will show as pending until they sign up via the invitation link.

### Members Status

You can overview members according to their status.

![Member status filter in ProtoPie's Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/c74b31b441e619b41e493582c43513447476b806-783x355.png/member-status.png)

#### Active

Active members are those who created an account and are part of your Enterprise environment. If you click on a member, you can access more detailed information, including which team(s) they are part of or when they used ProtoPie the last time.

![Active member in ProtoPie Enterprise Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/2ff1e62e5ac56dbafbef8b6e850f34f95699cdb7-789x713.png/active-member.png)

If you deactivate a member who has an editor role, their editor seat becomes available. They can use their account again once you activate it again.

#### Deactivated

Selecting members with a deactivated status lets you see which members can no longer access the Enterprise environment. To allow deactivated members to access the enterprise environment again, you must reactivate their accounts.

![ deactivated members in ProtoPie Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/a3fc36f1b7f349bd556f8978492a3e370bacfc04-1065x531.png/deactivated.png)

#### Pending

This filter displays members who have been invited to the Enterprise environment but havenât created their Enterprise account yet. Pending members canât use their enterprise access unless they sign up through the invitation link they have received.

![pending members in ProtoPie Enterprise Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/ee218e3ee109d8bd9ca94b0fe9c3f752b7a8db01-1053x343.png/pending.png)

There are three options available in the overflow menu next to each pending member:

- **Copy Invitation Link**: This option lets you quickly copy the invitation link associated with the pending member. If you prefer to share the invitation link directly without email, you can copy it and share it through other communication channels.

- **Resend**: If you need to resend the invitation email to the pending member, you can select the "Resend" option.

- **Cancel invite**: If you want to cancel the invitation for a specific member, you can choose the "Cancel invite" option. This will revoke the invitation and remove the member from the list of pending members.

### Assigning Service Admin Privileges

In ProtoPie Enterprise environments, you can **assign multiple service admins.** However, having at least one admin is required. If you would like to designate someone else as a service admin, and you are currently an admin yourself, you can easily make the change by adjusting their member type.

To change someone's member type to service admin, follow these steps:

1. Access **Organization settings**.

1. Navigate to the **Members** section.

1. Locate the member whom you wish to make a service admin.

1. Update their member type to **Service Admin**.

![Assigning the service admin role in ProtoPie Enterprise ](https://cdn.sanity.io/images/vidqzkll/production/ecfd76dc0a61ecd4d0a68f8659ef18126d25cbf4-1064x574.png/assign-service-admin.png)

 

## Managing Fonts in Organization Settings

![managing fonts](https://cdn.sanity.io/images/vidqzkll/production/dc421508965cd7d266591241d5cfffe87a0032c0-2000x917.png/custom_fonts.png)

### Uploading Custom Fonts to ProtoPie Cloud

To easily upload custom fonts to ProtoPie Cloud and make them accessible to all members of your organization, follow these steps. We support font file formats like TTF and OTF.

1. Go to Organization Settings within the organization space.

1. Navigate to the Fonts section.

1. Click the** Upload fonts** button to open the Upload fonts modal.

1. Add the font files by either dragging and dropping them into the modal or clicking "upload files" to select the font files from your device. 

  1. The selected fonts will be listed for upload.

  1. The font name, weight, and style fields will be automatically populated based on the information from the font files.

  1. To add more fonts, click the "Add more fonts" option at the bottom left corner of the modal.

  1. Remove fonts from the upload list by using the delete icon next to each uploaded font.

1. Click the "Next" button.

1. Take the time to carefully review and agree to ProtoPie's Terms of Service and Privacy Policy.

1. Finally, click the "Agree & Upload" button to add the fonts to the fonts list.

**Important**: Before adding new fonts, it is essential to verify that your organization possesses the legal rights to use and distribute the custom fonts being uploaded. ProtoPie cannot be held responsible for font licenses and their usage.

### Removing Custom Fonts from ProtoPie Cloud

As the service admin, you can easily remove custom fonts from the fonts list by following these steps:

1. Navigate to **Organization Settings** and access the **Fonts** section.

1. Locate the custom font you want to delete and open the three-dot menu.

1. Select the "**Remove**" option to remove the font from the list.

## Managing Security in Organization Settings

### Restricting Public Access to Prototypes

![Restricting public access to Pies in ProtoPie Enterprise](https://cdn.sanity.io/images/vidqzkll/production/e7a934fe0c366526c2b5cbc5b5c2738c11f9c624-786x572.png/public-access.png)

The **Public access to Pies **section provides the ability to control public access to prototypes for all editors simultaneously.

These options are enabled by default, allowing editors to share their prototypes with anyone with the link. However, if you prefer to maintain strict control over your prototypes within the ProtoPie Enterprise environment, you can disable this option to restrict access.

[Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#managing-access) about sharing prototypes.

### Configuring Session Duration and Inactivity Timeout

In **Session**, you can adjust the session duration for all invited members. Once the session duration expires, members will be automatically logged out.

Additionally, you can define a session inactivity timeout, which determines the period of inactivity before a member is logged out. This feature allows you to ensure optimal security by automatically logging out inactive members after a specified period of inactivity.

![Session section in ProtoPie Enterprise Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/ec7bf51cfab8378a9f0132d881235f5155da26ec-762x394.png/session.png)

### Configuring Account Management

Within your organization's security settings, you also have the option to allow members to delete their own accounts or restrict this option to service admins only.

![account management ](https://cdn.sanity.io/images/vidqzkll/production/392fd1272f557a476d9212f10867e4ec25313489-730x227.png/account management.png)

## Managing Authentication in Organization Settings

 You can access authentication settings and options to manage user sign-up methods in the **Authentication** section.

![Managing authentication settings in ProtoPie Enterprise](https://cdn.sanity.io/images/vidqzkll/production/3c45ec19596814e184738451bdf6166a78551747-794x460.png/authentication.png)

In this section, you have the ability to authorize members of your Enterprise environment to sign up and log in using either their email and password or through SSO (Single Sign-On) exclusively.

Under **Email & Password**, you can choose to authorize new members to join the Enterprise environment exclusively upon invitation from a service admin. Alternatively, you can enable sign-ups without an invitation or with email verification required, allowing team owners and/or team admins to invite new members. This gives them the autonomy to independently manage team membership without relying on the service admin for every new addition.

![Email and Password section in Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/441d86c955800f505c8ff8200d8b123f2dd93b35-705x465.png/email-password.png)

Additionally, you can choose to restrict which email domains invited members are allowed to use when signing up.

![allowed domains](https://cdn.sanity.io/images/vidqzkll/production/9fbcd08ab3be617869b2ecd9078052484b90f30f-721x407.png/allowed-domains.png)

### Configuring Single Sign-On (SSO)

If you prefer to use SSO for authentication, you can enable SAML or OIDC in the Single Sign-on (SSO) section. This allows users to sign in to ProtoPie Enterprise using their existing SSO credentials, providing a seamless and integrated login experience.

 [Learn more](https://www.protopie.io/learn/docs/enterprise/single-sign-on) about how to configure SSO for your Enterprise environment.

## Accessing Reports in Organization Settings

In the** Report** section, you can export member data in CSV format. This includes information about their accounts, like email addresses and roles, and insights into their activity, like account creation date, last login date, and invitation date. 

![Report section in Organization Settings ](https://cdn.sanity.io/images/vidqzkll/production/e3599cdb860e8f5c3cb7bb785c51bbf90de52338-2830x1638.png/report.png)

## Managing the General Information of Your Organization

In the **General** tab, you can view and edit the information about your organization, such as the name and logo of your enterprise environment.

Furthermore, if required, you can provide the contact details of the service administrator to facilitate communication for members seeking permissions, alterations in organization settings, and other tasks that are beyond their capabilities. 

![general information of your organization](https://cdn.sanity.io/images/vidqzkll/production/8e624e4cd7e7cad8e48754019775936f51a543f3-1045x681.png/general information.png)

You will also find information about your ProtoPie enterprise license, which includes the date when it will expire and the version of the application your organization is currently utilizing.  

![plan information](https://cdn.sanity.io/images/vidqzkll/production/1117c4641eeebc6ad57a4a2cc2d4147aba370080-1028x193.png/plan information.png)


---

---
title: "Service Admin"
url: https://www.protopie.io/learn/docs/enterprise/service-admin
---

# Service Admin

# Service Admin

The service admin is crucial in overseeing the entire ProtoPie Enterprise environment. They have full administrative privileges and manage members, teams, security, and authentication.

Learn more about [managing Organization settings](https://www.protopie.io/learn/docs/enterprise/organization-settings) as a service admin.

The comparison table below outlines the differences in privileges in ProtoPie Enterprise environments based on different roles:

- **Service admin**: the top-level role with complete administrative privileges. An Enterprise environment can have one or [multiple service admins](https://www.protopie.io/learn/docs/enterprise/organization-settings#assigning-service-admin-privileges).

- **Team owner**: the owner of a specific team within the Enterprise environment. Each Enterprise team has a single team owner.

- **Team admin**: Administrators of a specific team within the Enterprise environment. An Enterprise team can have one or multiple team admins.

- **Regular members**: Editor or viewer members of a team within the Enterprise environment.

Team members can manage all public and private projects they are a member of. Additionally, they can delete prototypes (made by others) in all public projects and private projects they are a member of.

If you are a member and have problems with your account or team, contact the service admin in your company.

## Setting Up ProtoPie Enterprise Environments

The setup process for ProtoPie Enterprise depends on your activated plan tier: On-Premises or Private Cloud.

**Private Cloud:**

1. Utilize the unique Enterprise URL that you received from our team: ***https://xxxxx.protopie.cloud***.

1. Access the setup form by entering the Enterprise URL in your browser.

1. Complete the form to configure your ProtoPie Enterprise environment and create your service admin account.

**On-Premises:**

1. Utilize the Enterprise URL provided by your IT team to install ProtoPie Enterprise.

1. Enter the Enterprise URL in your browser to access the setup form.

1. Fill out the form to establish your ProtoPie Enterprise environment and set up your service admin account.

If you face any difficulties or have questions during the setup process, please don't hesitate to contact [our support team](https://www.protopie.io/form/contact-us). We are here to assist you.


---

---
title: "Single Sign-On (SSO)"
url: https://www.protopie.io/learn/docs/enterprise/single-sign-on
---

# Single Sign-On (SSO)

# Configuring Single Sign-On (SSO)

The service admin can configure SSO for their ProtoPie Enterprise environment.

With SSO, members can access ProtoPie through an authentication source of choice, e.g., Okta, Auth0, or OneLogin. These are also known as identity providers (IdP). This way, companies can centralize providing access to ProtoPie Enterprise.

SSO is an authentication scheme allowing users to log in to applications and websites with a single set of credentialsâwithout having to manage multiple usernames and passwords. Many organizations and enterprises already included SSO in their internal policies to ensure security and convenience.

ProtoPie Enterprise supports two SSO protocols:

- SAML 2.0

- OpenID Connect (OIDC) â on top of OAuth 2.0

## Setting Up SAML SSO

In SAML terminology, ProtoPie is the service provider (SP) that has to communicate with your identity provider (IdP) for authentication.

To set this up, add ProtoPie to your IdP. This comes down to: enter the assertion consumer service URL (spAcsUrl) from ProtoPie in your IdP, and the IdP Metadata URL from your IdP in ProtoPie.

1. Go to **Authentication** in the **Service Admin Settings**.

1. Enable SAML.

1. Copy the assertion consumer URL.

![sso saml](https://cdn.sanity.io/images/vidqzkll/production/c95f07842bc0714f704420b2d457ede6b3fb0726-4350x2268.png/image.png)

How you add applications to your IdP differs per IdP. We outlined the steps for using Okta below.

### SAML SSO with Okta

Follow this easy step-by-step video tutorial from ProtoPie School to set up Single Sign-On (SSO) with Okta.

- [Setting up SAML SSO with Okta](https://learn.protopie.io/path-player?courseid=sso-test&unit=66ad187ca45abdea080df542Unit).

Alternatively, you can follow the instructions below:

1. Log in to Okta and go to the **Applications** page.

1. Click on the **Add Application** in the top left corner.


1. Click on **Create New App** in the top right corner.


1. Select **SAML 2.0** as the **Sign on method** and click on **Create**.


1. Enter ProtoPie as the app name under **General Settings**. For convenience, upload the[Â ProtoPie logo.](https://www.protopie.io/support/media-kit) Then click on **Next**.


1. Do the following regarding the SAML Settings.

  1. Paste the copied assertion consumer URL in both the **Single sign on URL** and **Audience URI (SP Entity ID)** fields.

  1. Select **EmailAddress** as the **Name ID format**.

  1. Enter **firstName** for the **Name**, and **user.firstName** for the **Value**. Then, click on **Add Another**.

  1. Enter **lastName** for the **Name**, and **user.lastName** for the **Value**.

  1. Click on **Next**.


1. SelectÂ **I'm a software vendor. I'd like to integrate my app with Okta**Â and click on **Finish**.


1. Assign users in the ProtoPie app in Okta. Go to the ProtoPie application, and click on the **Assignments** tab. Assign users by clicking on the **Assign** button.


1. Click on the **Sign On** tab and then on **View Setup Instructions**.


1. The** Identity Provider Single Sign-On URL **is basically the IdP Metadata URL you need. Copy this.


1. Go back to **Authentication** in the Service Admin Settings.

1. If you didn't already, enable SAML.

1. Paste the IdP Metadata URL you copied in your IdP.

1. Click on **Update**.

### SAML SSO with Another IdP

To set up SAML SSO with another IdP, as with Okta, use the assertion consumer service URL (spAcsUrl) from ProtoPie and IdP Metadata URL from your IdP. Refer to the documentation of your preferred IdP on how to add new applications.

### SAML SSO with Azure AD

1. Sign in to Azure and access **Azure Active Directory**.

2. Select **Enterprise applications** on the left.

![Select Enterprise applications on the left.](https://cdn.sanity.io/images/vidqzkll/production/01a78e1be886a5fd4add4d602dc449b5c6ec008c-2000x816.png/AzureAD-1.png)

3. Select **All applications** â **New application**.

![Select All applications â New application.](https://cdn.sanity.io/images/vidqzkll/production/bc81ca2e40063f0ad93f8bb429ee134a918c811b-1202x431.png/AzureAD-2.png)

4. In **Azure AD Gallery**, search and select **Azure AD SAML Toolkit** to add it.

- In the Name field, enter `ProtoPie`. Additionally, you can choose to upload the [ProtoPie logo](https://www.protopie.io/support/media-kit).

![In Azure AD Gallery, search and select Azure AD SAML Toolkit to add it.](https://cdn.sanity.io/images/vidqzkll/production/1667abdc96518f3a89a3ee4f770a945e65088b45-1318x506.png/AzureAD-3.png)

5. Once the Application is added, you can check the Overview of the added Application as follows. Then you can finalize the settings in the **Getting Started** menu.

![Finalize the settings in the Getting Started menu](https://cdn.sanity.io/images/vidqzkll/production/363e0318f28b24323da9fc76775f21cf9844cb77-2000x1101.png/AzureAD-4.png)

6. Select the **Assign users and groups** menu to set users or user groups.

![Select the Assign users and groups menu.](https://cdn.sanity.io/images/vidqzkll/production/4518a09a5595d9fe6cd231e5a24d23662f074404-2000x909.png/AzureAD-5.png)

7. Select the **Set up single sign-on** menu to begin the configuration of SSO. Select **SAML method**.

![Select SAML method.](https://cdn.sanity.io/images/vidqzkll/production/3ed3b0f0ee7ac98196a12f3ebcba96bd27b5e1ce-2000x991.png/AzureAD-6.png)

8. Select **Basic SAML Configuration Edit** to enter the values. Enter the following values. 

- Identifier (Entity ID): `https://PROTOPIE_DOMAIN/sp`

- Reply URL (Assertion Consumer Service URL): `https://PROTOPIE_DOMAIN/api/auth/callback/sso/saml`

  - These values are the same as those from `ProtoPie Admin Dashboard â Authentication â SAML â Assertion Consumer URL`.

- Sign on URL: `https://PROTOPIE_DOMAIN/api/auth/login/sso/saml`

![Set up SSO with SAML.](https://cdn.sanity.io/images/vidqzkll/production/142e11b8ee914a57e96ccf6d03475265e53e43e1-1541x651.png/AzureAD-7.png)

9. Copy the **App Federation Metadata URL** found in the **SAML Signing Certificate**.

![SAML Signing Certificate.](https://cdn.sanity.io/images/vidqzkll/production/d19b200066f934584ff7d28b65597e4cfdbc194f-1519x437.png/AzureAD-9.png)

10. Go to **Authentication â SAML** menu in ProtoPie Admin Dashboard to enable SAML and enter the following values:

- Authn Context: `urn:oasis:names:tc:SAML:2.0:ac:classes:unspecified`

- IdP URL (IdP Metadata URL): Enter `App Federation Metadata URL` you copied from above.

## Setting Up OIDC SSO

OpenID Connect (OIDC) is an authentication protocol built on top of the OAuth 2.0 framework.

Follow this easy step-by-step video tutorial from ProtoPie School to set up OIDC SSO.

- [Setting up OIDC SSO](https://learn.protopie.io/path-player?courseid=sso-test&unit=66b2a89ded9dcdd26f0f66abUnit)

Alternatively, you can follow the instructions below.

To set this up, add ProtoPie to your IdP. This comes down to: enter the callback URL (loginUrl) from ProtoPie in your IdP, and the authorization URL, token URL, client ID, and client secret from your IdP in ProtoPie.

1. Go to **Authentication** in the **Service Admin Settings**.

1. Enable OIDC.

1. Copy the callback URL.


How you add applications to your IdP differs per IdP. We outlined the steps for using Okta below.

### OIDC SSO with Okta

1. Log in to Okta and go to the **Applications** page.

1. Click on theÂ **Add Application** in the top left corner.


1. Click onÂ **Create New App**Â in the top right corner.


1. SelectÂ **OpenID Connect**Â as theÂ **Sign on method**Â and click onÂ **Create**.


1. Enter ProtoPie as the app name underÂ **General Settings**. For convenience, upload theÂ [ProtoPie logo](https://www.protopie.io/support/media-kit). Also, paste the copiedÂ callback URLÂ in theÂ **Login redirect URIs**Â field. Then click onÂ **Save**.


1. Assign users in the ProtoPie app in Okta. Go to the ProtoPie application, and click on theÂ AssignmentsÂ tab. Assign users by clicking on theÂ AssignÂ button.


1. Click on theÂ GeneralÂ tab. Copy both:Â client IDÂ andÂ client secret.


1. Click on theÂ **Sign OnÂ **tab. You need both the Authorization URL and Token URL. These two URLs do differ per IdP. For Okta, the Authorization URL has **${baseUrl}/oauth2/v1/authorize**Â structure and the Token URL has **${baseUrl}/oauth2/v1/token**Â structure. UseÂ **Issuer**Â under theÂ **OpenID Connect ID Token**Â for the base URL.Â [Learn more ](https://developer.okta.com/docs/reference/api/oidc/#composing-your-base-url)about how to compose your base URL.


1. Go back toÂ **Authentication**Â in theÂ **Service Admin Settings**.

1. If you didn't already, enableÂ OIDC.

1. Enter theÂ authorization URL,Â token URL,Â client ID, andÂ client secret.

1. Click onÂ **Update**.

### OIDC SSO with Another IdP

To set up OIDC SSO with another IdP, as with Okta, you need the Callback URL from ProtoPie, and the Authorization URL, Token URL, Client ID, and Client Secret from your IdP. Refer to the documentation of your preferred IdP on how to add new applications.

## Managing Members

With SSO enabled, still manage your members in ProtoPie Enterprise itself. Even though you add or remove users in your IdP, ProtoPie Enterprise does not reflect these changes automatically.

If you change a user's email address in the IdP, make the same change in ProtoPie Enterprise.

## FAQs


---

---
title: "Functions"
url: https://www.protopie.io/learn/docs/formulas/functions
---

# Functions

# Functions

Functions are like ready-made tools that perform specific tasks. They take in data as input, process it, and return a result.

Here are a few examples of what functions can do:

- Count the number of characters in a text.

- Search for a specific word in a text.

- Determine the smallest number between two numbers.

Functions in ProtoPie have a specific structure:

- `function(argument: TYPE)` â result: TYPE

- `function(argument1: TYPE, argument2: TYPE)` â result: TYPE

- `function(argument1: TYPE, argument2: TYPE, argument3: TYPE)` â result: TYPE

Functions usually use one or multiple arguments (data) as inputâthe values a function uses to perform a task. Arguments, as well as the result, are values that are always of a specific type. A type could be a text, number, or color.

There are various categories to choose from: 

- [Text](https://www.protopie.io/learn/docs/formulas/functions#text)

- [Math](https://www.protopie.io/learn/docs/formulas/functions#math)

- [Color](https://www.protopie.io/learn/docs/formulas/functions#color)

- [Type Conversion](https://www.protopie.io/learn/docs/formulas/functions#type-conversion)

- [Layers](https://www.protopie.io/learn/docs/formulas/functions#layers)

- [Relative Coordinates](https://www.protopie.io/learn/docs/formulas/functions#relative-coordinates)

- [Time & Date](https://www.protopie.io/learn/docs/formulas/functions#time-date)

## Learn More in ProtoPie School's Masterclass

Looking to learn more about using functions in ProtoPie? Join [ProtoPieâs Masterclass](https://learn.protopie.io/course/masterclass-in-advanced-prototyping-for-digital-dashboard) for detailed examples and guidance on using some of the functions listed in this documentation.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/formulas/getting-started
---

# Getting Started

# Formulas

With formulas and variables, you can create prototypes that truly come to life. Formulas are expressions that allow you to add logic to your interactions. From validating passwords to counting items in a shopping cart, and even calculating total account balances, formulas make it all possible.

With ProtoPie's formula capabilities, you can access layer properties, perform calculations, and utilize a wide range of functions for tasks like text manipulation and advanced mathematics.

Formulas are added using the formula input field. Simply include layer properties, functions, and variables as needed. Need a quick reference? Just click on the + icon to explore the available layers and variables at your disposal.

![formulaInput](https://cdn.sanity.io/images/vidqzkll/production/a62abc95580c233af991abaf23042562e0be4d2b-1076x1138.png/Screenshot 2026-02-05 at 10.57.03â¯PM.png)

New to formulas? Don't worry, we've got you covered! Here are some resources to help you make the most out of ProtoPie's Formulas.

- [Syntax](https://www.protopie.io/learn/docs/formulas/syntax) âÂ Just like any language, formulas have their own set of rules and principles. Learn the syntax to confidently craft your first formula.

- [Layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties) âÂ Access a wide range of layer properties to bring your interactions to life. Mastering layer properties is the first step towards creating dynamic prototypes.

- [Functions](https://www.protopie.io/learn/docs/formulas/functions) âÂ Take advantage of our predefined formulas that perform specific tasks. Functions process data and deliver results, making your prototypes even more powerful.

- [Use cases](https://www.protopie.io/learn/docs/formulas/use-cases) âÂ Explore practical examples of how formulas can be used effectively. Learn from real-world scenarios and apply the knowledge to your own projects.

## Difference Between Formulas & Variables

Formulas and variables work together seamlessly to enhance your prototypes. Here's a quick breakdown of their relationship:

Variables: Think of variables as handy "baskets" that hold values. They allow you to store and retrieve data, making it easier to reuse information throughout your prototype. Variables can be used independently or in conjunction with formulas. For example, you use formulas to retrieve a value stored in a variable.

Formulas: Formulas are expressions that calculate and "return" a result. They are powerful tools for creating dynamic interactions. You can use formulas to perform calculations, manipulate text, and accomplish various tasks. Formulas can also include variables to access stored values.

The synergy between formulas and variables allows you to take your prototypes to the next level. Variables store values that can be utilized by formulas, while formulas can even be stored within variables for reuse across scenes.

In summary, formulas and variables complement each other, offering flexibility and efficiency in your prototype development process.

[Learn more](https://www.protopie.io/learn/docs/variables/getting-started) about variables.

## Learning the Basics

Formulas may seem intimidating, but they are more accessible than you think. With just a few formulas, anyone can create dynamic interactions!

In this video tutorial, you'll learn how to make an engaging interaction using ProtoPie. Watch as we demonstrate how to move a rectangle layer to the position of another rectangle layer, no matter where it is in the scene.

Learn more about [layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties) and doing [simple calculations](https://www.protopie.io/learn/docs/formulas/syntax#doing-calculations).

[Video: Formula > Formula  Video](https://www.youtube.com/watch?v=9F5EKS5gt2o)

## Practicing with Examples

### Making a Tab Bar

To make responses work dynamically, use formulas instead of fixed values. This video tutorial shows you how to animate a simple tab interaction using formulas. 

Learn more about [layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties) and doing [simple calculations](https://www.protopie.io/learn/docs/formulas/syntax#doing-calculations).

![formula menu](https://cdn.sanity.io/images/vidqzkll/production/ae4395251df7916bff2ce6f7a58c425dcec4706a-1076x228.gif/formula_menu.gif)

[Video: Formula > Tab Menu  Video](https://www.youtube.com/watch?v=0nZU634cIdQ)

### Using the Text from the Input Layer

You can also use formulas to display the text information stored in a variable. This video tutorial shows you how you can type in a text and display it somewhere else using a simple formula.

Learn more about [input layers](https://www.protopie.io/learn/docs/basic-features/layers#input-layer) and [layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties).

![formula input](https://cdn.sanity.io/images/vidqzkll/production/a811757e78bc186eadc71c6e2b57f88645966179-1076x540.gif/formula_input.gif)

[Video: Formulas > Text Input > Video](https://www.youtube.com/watch?v=nGIGjanAXxA)

Looking for practical use cases? [Learn more](https://www.protopie.io/learn/docs/formulas/use-cases) from practical use cases on formulas.


---

---
title: "Layer Properties"
url: https://www.protopie.io/learn/docs/formulas/layer-properties
---

# Layer Properties

# Layer Properties

When working with formulas, you have the option to utilize various layer properties, including but not limited to position, height, width, and opacity.

### Using Layer Properties

To refer to a layer, use backticks (`) around the layer name. 
To reference a layer property, add a period (.) followed by the property after the second backtick.


---

---
title: "Syntax"
url: https://www.protopie.io/learn/docs/formulas/syntax
---

# Syntax

# Syntax

Just like human languages, formulas in ProtoPie have their own set of rules and principles. These rules, known as syntax, govern how different elements such as text, numbers, layer properties, and variables are combined to create a formula.

Think of syntax as the framework that guides you in assembling these elements to achieve the desired outcome. By understanding and following the syntax rules in ProtoPie, you'll be able to create powerful and dynamic formulas that bring your prototypes to life.

## Using Literal Values

You need to follow specific rules when using elements such as layer properties, text, and numbers in formulas.

### Layer property

To refer to a layer, use backticks (`) around the layer name. To avoid confusion, we strongly recommend using unique names in layers.

To use a layer property, add a period (.) after the second backtick followed by the property.

[Learn more](https://www.protopie.io/learn/docs/formulas/layer-properties) about layer properties.



### Text

Use double quotation marks (") around the text.



### Text with multiple lines

To add a line break, add "\n" between words or characters.



### Number

Use Arabic numerals (0-9) only.



### Color

Use colors in the #FFFFFF format (hex color code).

### Variable

To refer to a variable, use the variable name as it is. A variable name can only contain Latin alphabetical letters, numbers, and underscores.

[Learn more](https://www.protopie.io/learn/docs/variables/getting-started) about variables.



## Doing Calculations

To do simple calculations, use the basic arithmetic (+, -, *, /) and modulo (%) operations.



### Arithmetic Operations

The basic arithmetic operations for numbers are addition (+), subtraction (-), multiplication (*), and division (/).

### Modulo Operation

To calculate the remainder of a division, use the modulo operation (%). For example, 5 % 2 results in 1, simply because 5 divided by 2 has a quotient of 2 and a remainder of 1.

## Combining Text

Arithmetic operations usually apply to numbers. However, to combine text, it's possible to use addition (+). When a text is "added" to another text, the result is a new text with the two texts combined.

### Text + Text

Use the addition (+) sign to combine two or more texts. As a reminder, always use double quotation marks (") around the text.



### Text + Number

Use addition (+) sign to combine two or more texts and numbers. The result is always a new text.


---

---
title: "Formulas Use Cases"
url: https://www.protopie.io/learn/docs/formulas/use-cases
---

# Formulas Use Cases

# Formulas Use Cases

Explore the practical application of formulas for various use cases. Learn how to effectively use the correct syntax, layer properties, and functions. Experience the prototypes firsthand by trying them out and downloading them to observe their interactions.

Learn more about [formulas](https://www.protopie.io/learn/docs/formulas/getting-started) and [variables](https://www.protopie.io/learn/docs/variables/getting-started).

Find the use case you need below:



- [Validating an email address](https://www.protopie.io/learn/docs/formulas/use-cases#validating-an-email-address)

- [Minimum password length](https://www.protopie.io/learn/docs/formulas/use-cases#minimum-password-length)

- [Showing & hiding a password](https://www.protopie.io/learn/docs/formulas/use-cases#showing-hiding-a-password)

- [Countdown timer](https://www.protopie.io/learn/docs/formulas/use-cases#countdown-timer)

- [Random shuffle](https://www.protopie.io/learn/docs/formulas/use-cases#random-shuffle)

- [Checking a bank account balance](https://www.protopie.io/learn/docs/formulas/use-cases#checking-a-bank-account-balance)

- [Expanding a card in a list](https://www.protopie.io/learn/docs/formulas/use-cases#expanding-a-card-in-a-list)

Looking for variable-specific use cases? Check out the [use cases involving variables](https://www.protopie.io/learn/docs/variables/use-cases).

Find tips, tricks, and solutions about formulas and variables that other users have shared before in our communities.



- [ProtoPioneers Community](https://community.protopie.io/home)

- [ProtoPie YouTube channel](https://www.youtube.com/c/ProtoPie/featured)

- [ProtoPie Users on Facebook](https://www.facebook.com/groups/ProtoPieUsers/)

## Validating an Email Address

Validate a text, e.g., an email address, as part of a signup process. Check whether specific characters or a keyword are present in a text. In this case, to validate if the input is an email address, check whether "@" is present with the indexOf function.

![Validating email address](https://cdn.sanity.io/images/vidqzkll/production/086c082b33e44ce41ede65166d4ff5886a8ec483-1450x990.gif/validating an email adress.gif)

[Try the prototype](https://cloud.protopie.io/p/d38f6337d7) yourself.

Used functions: indexOf.

Learn more about [functions](https://www.protopie.io/learn/docs/formulas/functions), [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition), and the [Focus trigger](https://www.protopie.io/learn/docs/interactions/triggers#focus).

## Minimum Password Length

To enhance security, passwords often should have a minimum character length. Check whether an input exceeds a certain number of characters with the length function.

![minimun password length](https://cdn.sanity.io/images/vidqzkll/production/cbdaf2430ef93e2c26eec027ab7aea7f30106cc1-1450x990.gif/minimun password length.gif)

[Try the prototype](https://cloud.protopie.io/p/d38f6337d7) yourself.

Used functions: length.

Learn more about [functions](https://www.protopie.io/learn/docs/formulas/functions), [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition), and the [Focus trigger](https://www.protopie.io/learn/docs/interactions/triggers#focus).

## Showing & Hiding a Password

To verify whether you are typing the correct password or not, you need to show and hide the password. Do this by using the text property of an input layer.

![show hide password](https://cdn.sanity.io/images/vidqzkll/production/c3dff07d6042b3d0c15c702d2826e13dd827d4e4-1450x990.gif/show hide password.gif)

[Try the prototype](https://cloud.protopie.io/p/0a49ac128d) yourself.

Learn more about [layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties), [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition), and the Detect trigger.

## Countdown Timer

Make any countdown timer you can imagine. Adjust the repeat of the Text response to set the duration of the countdown timer.

![countdown timer](https://cdn.sanity.io/images/vidqzkll/production/2a7b8b592cb8301bce0f1089ba03f30f72dcb9f2-1450x990.gif/countdown timer.gif)

[Try the prototype](https://cloud.protopie.io/p/e0b7b6ade8) yourself.

Used functions: number.

Learn more about [functions](https://www.protopie.io/learn/docs/formulas/functions), [layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties), and [arithmetic operations](https://www.protopie.io/learn/docs/formulas/syntax#arithmetic-operations).

## Random Shuffle

Display a letter or number randomly based on a fixed set of letters and numbers.

![random shuffle](https://cdn.sanity.io/images/vidqzkll/production/41ba8c67faa55dfcb5f1b5c557ac517200db5dbc-1450x990.gif/random shuffle.gif)

[Try the prototype](https://cloud.protopie.io/p/ff5385b53a) yourself.

Used functions: right, left, randomInt.

Learn more about [functions](https://www.protopie.io/learn/docs/formulas/functions) and the [Start trigger](https://www.protopie.io/learn/docs/interactions/triggers#start).

## Checking a Bank Account Balance

To check whether a bank account balance is positive or negative, verify whether a number is above or below 0.

![checking a bank account balance](https://cdn.sanity.io/images/vidqzkll/production/80abdcec342199d2db11c81a7a109803ce7926be-1450x990.gif/checking a bank account balance.gif)

[Try the prototype](https://cloud.protopie.io/p/d5de1415a5) yourself.

Functions used: sign.

Learn more about [arithmetic operations](https://www.protopie.io/learn/docs/formulas/syntax#arithmetic-operations), [functions](https://www.protopie.io/learn/docs/formulas/functions), and [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition).

## Expanding a Card in a List

Expand a card in a scrollable card list regardless of the scroll position of the scroll container, with the card moving to the top making space for other content.

![expanding a card](https://cdn.sanity.io/images/vidqzkll/production/62d4df4560c39900000cba63f9aa50581c367455-1450x990.gif/expanding a card in a list.gif)

[Try the prototype](https://cloud.protopie.io/p/35164ca834) (made by one of our users, Nestor) yourself.

Used functions: toLayerX, toLayerY.

Learn more about [functions](https://www.protopie.io/learn/docs/formulas/functions) and [arithmetic operations](https://www.protopie.io/learn/docs/formulas/syntax#arithmetic-operations).


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/import/getting-started
---

# Getting Started

# Import

ProtoPie allows you to import designs from Sketch, Adobe XD and Figma with just a few clicks.

Use the ProtoPie plugins forÂ [Figma](https://www.figma.com/community/plugin/908870217222043020/ProtoPie-Plugin),Â [Sketch](https://r.protopie.io/sketch-latest-link/), andÂ [Adobe XD](https://xd.adobe.com/landing/plugin-download/en/desktop.html?pluginId=cec71af9) to import your designs quickly and flexibly.

## Getting Started

- Plugin (recommended): Install the ProtoPie plugin for Figma, Sketch, or Adobe XD, and open the plugin in the tool that you want to import from.

- Legacy: Open the Sketch or Figma file that you would like to use for importing and open ProtoPie Studio. Select **Import** from the file menu in ProtoPie.

![import](https://cdn.sanity.io/images/vidqzkll/production/fb810beecd7f9004de31e9b5c5dfdbc142ee06f5-1270x802.png/Import.png)

Learn more about importing from [Figma](https://www.protopie.io/learn/docs/import/importing-from-figma), [Sketch](https://www.protopie.io/learn/docs/import/importing-from-sketch), and [Adobe XD](https://www.protopie.io/learn/docs/import/importing-from-adobe-xd).

## FAQs


---

---
title: "Importing From Adobe XD"
url: https://www.protopie.io/learn/docs/import/importing-from-adobe-xd
---

# Importing From Adobe XD

# Importing From Adobe XD

Import your designs from Adobe XD into ProtoPie using the [Plugin](https://www.protopie.io/learn/docs/import/importing-from-adobe-xd#proto-pie-plugin-for-adobe-xd).

Install the [ProtoPie plugin for Adobe XD](https://adobe.com/go/xd_plugins_discover_plugin?pluginId=cec71af9) and open the plugin in Adobe XD.

## ProtoPie Plugin for Adobe XD

[Download and install ](https://www.protopie.io/adobexd)the ProtoPie plugin for Adobe XD, which requires ProtoPie 7.0 or higher.

With the ProtoPie plugin for Adobe XD, you have lightning speed and flexibility at your fingertips. Import your designs from Adobe XD into ProtoPie, all done locallyâwithout any latency.

Control what you import. Import artboards as scenes, and objects with the same layer hierarchy, positioning, and constraints as in Adobe XD.

For the best performance, keep Adobe XD open and visible on your desktop while importing your designs into ProtoPie.

First time? Try the ProtoPie plugin for Adobe XD with this [example file](https://r.protopie.io/en/adobe-xd-plugin/marketing-file/).

### Supported Properties

- Visibility

- Lock

- Position

- Size

- Rotation

- Opacity

- Constraints

- Fill (solid color & image)

- Borders

- Shadow

[Learn more](https://www.protopie.io/learn/docs/basic-features/layers#layer-property) about layer properties in ProtoPie.

The ProtoPie plugin for Adobe XD allows you to:

- Import one or multiple artboards and objects.

- Import artboards as scenes.

- Import what you selected.

- Import vector layers as SVG.

- Import text layers as SVG that can be converted to text layers.

- Import constraints as constraints.

![general-adobexd-plugin](https://cdn.sanity.io/images/vidqzkll/production/f94cf2869e05c0f329060a9aa3e60f85664366b4-2140x1182.gif/general_protopie_plugin_for_adobe_xd__1_.gif)


---

---
title: "Importing From Figma"
url: https://www.protopie.io/learn/docs/import/importing-from-figma
---

# Importing From Figma

# Importing Designs from Figma

There are two ways to import your designs from Figma into ProtoPie.

- [Via the p](https://www.figma.com/community/plugin/908870217222043020/protopie)[lugin](https://www.figma.com/community/plugin/908870217222043020/protopie) (recommended): Install the ProtoPie plugin for Figma and open the plugin in Figma.

- [Legacy import](https://www.protopie.io/learn/docs/import/importing-from-figma#legacy-figma-import): First, open the Figma file you want to import. Then, open ProtoPie Studio and select **Import** from the File menu.

### Key Differences Between Plugin and Legacy Import

The ProtoPie plugin for Figma allows you to:

- Import one or multiple sections, frames and objects.

- Import top-level frames as scenes.

- Import what you selected.

- Import vector layers as SVG.

- Import text layers as SVG that can be converted to text layers.

- Import constraints as constraints.

- Import Auto Layout properties.

- Import Figma components as reusable, linked components with variant support (Component Mode).

## The ProtoPie Plugin for Figma

![general-plugin-for-figma](https://cdn.sanity.io/images/vidqzkll/production/55f37db660f9489f8b537156fa5ea59580cb4a51-1836x1080.gif/1104.gif)

Import your designs from Figma into ProtoPie, all done locallyâwithout latency.

[Download and install](https://www.protopie.io/figma) the ProtoPie plugin for Figma, which requires ProtoPie 9.5.0 or higher.

Here are a few tips:

- Keep both Figma and ProtoPie open and visible on your desktop while importing your designs into ProtoPie for the best performance.

- When importing, use top-level frames as scenes and objects with the same layer hierarchy, positioning, and constraints as in Figma.

Hereâs whatâs new with the import experience: 

Items are now imported individually and appear in ProtoPie Studio as soon as theyâre ready. Previously, all items were processed at once and only became visible after everything finishedâthis update makes importing faster and more seamless.

### Supported Properties

- Visibility

- Lock

- Position

- Size

- Rotation

- Opacity

- Constraints

- Fill (solid color & image)

- Borders

- Shadow

- Auto Layout (core properties)

[Learn more](https://www.protopie.io/learn/docs/basic-features/layers#layer-property) about layer properties in ProtoPie.

The plugin also supports importing these elements:

- Sections

- Main components - when Component Mode is enabled, main components are imported directly to your ProtoPie Library as reusable components

- Component instances - stay linked on the canvas as references to Library components

- Component variants - imported as separate components with variant support

## Legacy Figma Import 

The legacy import allows you to import all layers, or only those marked for export, from your Figma files. This function requires ProtoPie 9.1.0 or higher due to recent structural changes in Figma.Â [Learn more](https://help.figma.com/hc/en-us/articles/360040028114)Â about marking for export in Figma. 

### Looking to improve your skills in managing large-scale projects and resources effectively?

Learn to import only essential assets from Figma or other design tools, optimize the prototype's performance, and reduce unnecessary clutter with our newest [Mobile Game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass).

If you wish to explore further, [join the ProtoPie Masterclass](https://learn.protopie.io/course/masterclass-in-advanced-prototyping-for-digital-dashboard?__s=2hdlh416jfc4vtrb5g2a&utm_source=drip&utm_medium=email&utm_campaign=ProtoPie+School%3A+Masterclass+in+advanced+prototyping+%E2%80%94+Get+early+access%21) for free and learn advanced techniques and strategies to take your ProtoPie skills to the next level. Our expert instructor will guide you through the best practices for creating successful projects. Sign up now and become a ProtoPie power user!

## FAQs


---

---
title: "Importing From Sketch"
url: https://www.protopie.io/learn/docs/import/importing-from-sketch
---

# Importing From Sketch

# Importing From Sketch

There are two ways to import your designs from Sketch into ProtoPie.

- [Plugin](https://www.protopie.io/learn/docs/import/importing-from-sketch#proto-pie-plugin-for-sketch) (recommended): Install the [ProtoPie plugin for Sketch](https://r.protopie.io/sketch-latest-link/) and open the plugin in Sketch.

- [Legacy](https://www.protopie.io/learn/docs/import/importing-from-sketch#legacy-sketch-import): Open the Sketch file that you would like to use for importing and open ProtoPie Studio. Select **Import** from the file menu in ProtoPie.

## ProtoPie Plugin for Sketch

[Download and install](https://www.protopie.io/sketch) the ProtoPie plugin for Sketch, which requires ProtoPie 7.0 or higher. [Learn more](https://www.sketch.com/docs/plugins/)* *about* *installing plugins for Sketch.

With the ProtoPie plugin for Sketch, you have lightning speed and flexibility at your fingertips. Import your designs from Sketch into ProtoPie, all done locallyâwithout any latency.

Control what you import. Import artboards as scenes, and objects with the same layer hierarchy, positioning, and constraints as in Sketch.

For the best performance, keep Sketch open and visible on your desktop while importing your designs into ProtoPie.

First time? Try the ProtoPie plugin for Sketch with this [example file](https://r.protopie.io/en/sketch-plugin/marketing-file/).

### Supported Properties

- Visibility

- Lock

- Position

- Size

- Rotation

- Opacity

- Constraints

- Fill (solid color & image)

- Borders

- Shadow

[Learn more](https://www.protopie.io/learn/docs/basic-features/layers#layer-property) about layer properties in ProtoPie.

### Differences Between the Plugin and Legacy Import

The ProtoPie plugin for Sketch allows you to:

- Import one or multiple artboards and objects.

- Import artboards as scenes.

- Import what you selected.

- Import vector layers as SVG.

- Import text layers as SVG that can be converted to text layers.

- Import constraints as constraints.

![sketch-general-plugin](https://cdn.sanity.io/images/vidqzkll/production/7a24b822b5c1fd94a9959c530d3094cc9a01eaf9-1946x1416.gif/CleanShot_2021-04-05_at_12.10.29.gif)

## Legacy Sketch Import

The legacy Sketch import allows you to import all layers, or only the layers that have been marked as exportable, from your Sketch files.


---

---
title: "ProtoPie Genie"
url: https://www.protopie.io/learn/docs/import/protopie-genie-plugin-figma
---

# ProtoPie Genie

# ProtoPie Genie

[**ProtoPie Genie**](https://www.figma.com/community/plugin/1360046269541821005/protopie-genie-beta) is a Figma plugin that enhances your design quality and workflow by enabling dynamic interactions directly with your Figma prototypes. With ProtoPie Genie, you can quickly create interactive elements, test various scenarios, and deliver compelling prototypes that effectively showcase your designs.

## Overview

ProtoPie Genie simplifies dynamic interaction testing, accelerates prototype delivery, and elevates prototype experiences through:

- **Fast prototype delivery:** Transform static designs into interactive prototypes quickly.

- **Dynamic interaction testing:** Test various scenarios and interactions seamlessly.

- **Impressive prototyping experience:** Impress your team, clients, and stakeholders with prototypes that feel alive.

## Getting Started

Follow these instructions to install the ProtoPie Genie plugin.

1. Visit the [Figma Community page](https://www.figma.com/community/plugin/1360046269541821005/protopie-genie-beta).

1. Choose "Open in..." to select the appropriate file for future tasks.

1. Click âRunâ to launch âProtoPie Genieâ.

Alternatively, right-click in Figma, navigate to the plugins menu, and select "ProtoPie Genie.â 

![How to Get Started?](https://cdn.sanity.io/images/vidqzkll/production/60af64507d17fae167486a3b1a39c4de6fee97ec-1434x794.png/Screenshot 2024-05-13 at 11.16.46â¯AM.png)

## Key Features

ProtoPie Genie allows you to incorporate a variety of interactive elements into your prototypes, enhancing user engagement:

- **Text Input:** Capture user input directly within the prototype and display it in real time.

- **Camera:** Integrate real-time camera views for immersive interactions.

- **Voice:** Implement speech-to-text and voice command functionalities for intuitive user experiences.

- **Maps:** Easily incorporate customizable maps into your designs.

- **Web embed:** Embed web content, such as videos, to enrich the user experience.

### Adding Interactive Elements

Below are steps to add specific features such as text input, camera views, voice interaction, maps, and web embeds.

#### Adding Text Input

Transform text objects into interactive input fields to simulate user interactions.

**Steps:**

1. Select the text object you want to convert into an input field.

1. Click the **âText inputâ** button to set the value source.

1. Click **âCreate interactionâ** to activate the input field.

1. Click **âAddâ** in the output field section to assign output items.

1. Choose a text object for displaying the output.

1. Preview the interaction in your browser.

#### Adding Camera Views

Integrate live camera views into your prototypes.

**Steps:**

1. Choose a rectangle shape for the camera area.

1. Select front or back camera view.

1. Insert a rectangle or ellipse shape for the shutter button.

1. Click **âCreate interaction**â to finalize the setup. 

#### Adding Voice Interaction

Incorporate voice recognition into your prototype.

**Steps:**

1. Choose a rectangle or ellipse shape for the listening button.

1. Select the language for speech-to-text.

1. Assign a text object for the transcribed text.

1. Click **âCreate interaction**â to implement voice interaction.

#### Adding Live Maps

Integrate interactive maps with customizable settings.

**Steps:**

1. Choose a rectangle shape for the map display.

1. Search and select a location to display on the map.

1. Customize map style and zoom level.

1. Click **âCreate interactionâ** to finalize the map integration.

#### Adding Web-Embeds

Embed videos and other web content seamlessly.

**Steps:**

1. Choose a rectangle shape for the web embed.

1. Enter the URL starting with `https://`. YouTube and Vimeo links will show video control settings.

1. Click **âCreate interactionâ** to add the web embed.

## Previewing Interactions

Previewing interactions in Figma with the ProtoPie Genie plugin is straightforward. You can preview single and multiple interactions directly in your browser or device.

**Previewing a Single Interaction**

1. Navigate to the **âInteractionsâ** tab to view the list of created interactions.

1. Click **âPreviewâ** to open the selected interaction in your default browser.

1. For device preview, click **âOpen in deviceâ** and scan the QR code.

**Previewing Multiple Interactions**

1. In Figma, create a workflow in the **âPrototypeâ** tab and name it as needed.

1. Return to the **ProtoPie Genie plugin** and open the **âInteractionsâ** tab.

1. Select the appropriate workflow and click **âPublish the selected flowâ** to preview all interactions.

## Supported Figma Objects

The ProtoPie Genie plugin supports a wide range of Figma objects, including:

- Text

- Rectangle

- Frame

- Group

- Component

- Instance

- Boolean

- Vector

- Ellipse

## Supported Figma Interactions

The ProtoPie Genie plugin seamlessly converts **"On Click"** and **"Navigate to"** Figma interactions during the preview, ensuring a comprehensive understanding of your design's interactive elements.

## Unsupported Figma Objects & Properties

Certain Figma objects and properties are not currently supported:

- **Unsupported Objects**: Star, Line, Polygon, Video.

- **Unsupported Properties**: Visibility, Lock, Position, Size, Rotation, Opacity, Constraints, Fill (solid color & image), Borders, Shadow.

- **Known limitation:** Gradients, effects (blur, inner shadow, layer effects), object rotation, font issues, image sizing, and video support may have limitations.

## ProtoPie Genie Player

**ProtoPie Genie Player** is a free app designed to complement the **ProtoPie Genie** plugin for Figma. Easily view, experience, and test your prototypes on iOS or Android devices. Access prototypes stored in the cloud, save them locally, and more â all from your mobile or tablet device!

With ProtoPie Genie Player, you can now seamlessly preview and interact with your Figma prototypes in real-time on your device.

Get ProtoPie Genie Player for [**iOS**](https://apps.apple.com/kr/app/protopie-genie-player/id6504745909?l=en-GB) and [**Android**](https://play.google.com/store/apps/details?id=io.protopie.genie.player&hl=en) devices.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/interaction-libraries/getting-started
---

# Getting Started

# Interaction Libraries

Interaction libraries serve as convenient repositories of components within [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/getting-started). These libraries allow you and your team members to effortlessly and swiftly utilize component instances in your prototypes.

![interaction-libraries](https://cdn.sanity.io/images/vidqzkll/production/5c73d2eee43caa6bf79463e130be3aa65e73e5ee-2175x1269.png/interaction-libraries.png)

There are three distinct types of interaction libraries available in ProtoPie:

1. **Team Libraries** ([Pro plan](https://www.protopie.io/plans/pro) and [Enterprise plan](https://www.protopie.io/plans/enterprise)): Team libraries enable collaboration within a team. Any editor within the team can create and manage team libraries, allowing multiple team members to contribute and modify the components. The components stored in team libraries are accessible to all editors within the team, fostering seamless collaboration and consistency.

1. **Personal Libraries** (all plans): Personal libraries are designed for individual use. You have the ability to create personal libraries within your personal space in the cloud. These libraries are exclusively available for your use, allowing you to organize and reuse components according to your specific needs and preferences.

1. **Public Libraries** (all plans): Public libraries are accessible to all users and serve as standardized libraries for commonly used components. Examples of public libraries include Material Design and iOS interaction libraries. You can leverage the components from these libraries to streamline your prototyping process and align with established design patterns.

### Creating Interaction Libraries

To create a new interaction library, follow these simple steps:

1. Navigate to the **Component Panel** and locate the "**Search Components..."** section.

1. On the right side of the "**Search Components..."** section, you will see a **bookshelf icon**. Click the icon, then click the "+" button to start the creation process.

1. Provide a name for your library that accurately describes its purpose. Optionally, you can add a description to provide additional context or details about the library.

1. Once you have specified the name and description, finalize the creation by clicking on the Create button.

![CreateLibrary](https://cdn.sanity.io/images/vidqzkll/production/05adbe1ac1779e0220bd13d89574613127d6ec21-875x749.png/interaction libraries.png)

A new library window will open and you will notice the Currently Editing label displayed in the component panel. At the top of the window, you will see a prominent  banner. This banner serves as a visual indicator that you are in **library edit mode.**

![LibraryEditMode](https://cdn.sanity.io/images/vidqzkll/production/f5368ac806460a1aad49c9a868d1699282311f67-2004x1106.png/Interaction Edit.png)

### Publishing Interaction Libraries

To ensure that you and your team can access the latest components in your interaction libraries, it is important to publish your changes to the cloud. Follow these steps:

1. **Save your changes**: Before publishing, make sure to save any modifications or updates you have made to the interaction library.

1. **Locate and Click on the Publish button:** You can find the Publish button in two different locations. It is positioned on the right side of the purple banner within the library window, or alternatively, in the top right corner of ProtoPie Studio. Once you have located the Publish button, click on it to initiate the publishing process.

![HowtoPublish](https://cdn.sanity.io/images/vidqzkll/production/a279198dcea1ffdde7515681542b9606a8750ca8-1450x800.png/publish.png)

### Adding Component Instances

To add instances of a component to your prototype, follow these simple steps:

1. **Drag and drop**: Begin by selecting a component from any interaction library in the component panel. Once you have chosen the desired component, simply drag it from the panel and drop it onto the canvas of your scene.

1. **Multiple libraries, multiple instances**: You can also create instances of components from multiple interaction libraries.

![UseComponents](https://cdn.sanity.io/images/vidqzkll/production/d34c10967aa737c350d472f914aca413d198c73a-1450x800.png/adding_component_instances.png)

### Updating Interaction Libraries

To ensure that your prototypes remain up-to-date with the latest changes in the interaction libraries, follow these steps:

1. **Select the libraries to update**: Click on the Update Library icon to open the Update Library window. Here, you can choose which interaction libraries you want to update to include the latest changes.

1. **Manual refresh**: Alternatively, you have the option to manually refresh the libraries by clicking on the refresh icon located in the top right corner. This will allow you to check for any new updates to the libraries.

If any of the interaction libraries, which contain components used as instances in your prototypes, have been updated, you will receive a notification on the Update Library icon.

![UpdateLibrary](https://cdn.sanity.io/images/vidqzkll/production/3060769106d48b6ce5c82b5d0bde5bc8ea05aa7c-1068x586.png/updating interaction libaries.png)

### Export as New Library

Creating a library doesn't always require you to add components individually. If you already have a Pie with local components, you can conveniently export it as a new library in just a few steps:

1. **Click on File**: Open the menu and navigate to the File option.

1. **Select Export as New Library**: Choose the Export as New Library option from the menu. By exporting your Pie as a new library, you can effortlessly transfer all the components it contains into the library at once.

![ExportNewLibrary](https://cdn.sanity.io/images/vidqzkll/production/892a3df917d68bec80abc9e127993965ec9b1696-1450x800.png/export_as_new_library.png)

### Export to Library

![Export to library](https://cdn.sanity.io/images/vidqzkll/production/cbef9d760d475cc0882af9b1d17ff29e6576b462-1202x694.png/Export to library 1.png)

Besides exporting local components as a new library, you can export local components in a Pie to an existing library by clicking on the** Export to Library **icon in the Local Components section.

![Export to Library Window](https://cdn.sanity.io/images/vidqzkll/production/e468bb86017d0d8052e0b8edd48b0c8bf15c20b9-1732x1270.png/Export to library 2.png)

In the Export to Library window, you can easily choose one or multiple components that you want to export. Then, select the desired library to which you want to export these components. If you want to immediately make the exported library available for use, you can choose the option to publish it right after exporting.

### Searching and Filtering Libraries

You can now search for specific libraries and select which libraries to display in the panel via the dropdown menu in the library settings modal. This enhanced functionality helps you locate and focus on the libraries you need with ease.

![Filter Libraries 1](https://cdn.sanity.io/images/vidqzkll/production/8b898cbb34a8652cb5d302211a91c3b5d8fa01ce-1874x1342.png/Filter Libaries 1.png)

![Filter Libraries 2](https://cdn.sanity.io/images/vidqzkll/production/4ff01301382561e204ee54f7bac4fdcc00cf7850-1440x1494.png/Filter Libraries 2.png)

### Handling Conflicts in Team Libraries 

When multiple team members are simultaneously making changes to a team library in ProtoPie, conflicts may arise. If someone has already published their changes to the same library that you are currently editing, a warning message will be displayed. To handle conflicts, you have two options:

1. **Overwrite with your own changes: **If you choose this option, your own version of the library will become the latest version, replacing the changes made by others.

1. **Update the library to the new version**: If you select this option, the new version of the library, which includes the changes made by others, will be applied. Your own changes will be discarded in favor of the latest version.


![ConflictControl](https://cdn.sanity.io/images/vidqzkll/production/0c03e1a69987075a755823da294947ea3179b18c-1580x870.png/image.png)


---

---
title: "Managing Interaction Libraries"
url: https://www.protopie.io/learn/docs/interaction-libraries/managing-interaction-libraries
---

# Managing Interaction Libraries

# Managing Interaction Libraries

### Changing Name and Description

If you want to change the name or description of an interaction library, simply click on the overflow menu and View in Cloud button.

![ViewinCloud](https://cdn.sanity.io/images/vidqzkll/production/98f4566086d2e8f140070b84b9084c45c007662d-746x271.png/Components.png)

As the library owner, you can change the name and description of an interaction library by clicking on the settings icon in the top of the left panel in Cloud. You can also upload a library image.

![LibrarySetting](https://cdn.sanity.io/images/vidqzkll/production/31dc1963caebb92052a375cc2c4d1b136bbda2bb-1580x870.png/LibrarySetting.png)

### Version History

You can see all previous versions by clicking on the Version History button in the left panel. The versions with the lightning icons are the ones that have been published and the ones without are the ones that have been saved but not published.

![VersionHistory](https://cdn.sanity.io/images/vidqzkll/production/7adcd360d6b708225d4b000055dd9cc0b9d91f50-1580x870.png/VersionHistory.png)

![OpenStudio](https://cdn.sanity.io/images/vidqzkll/production/a06e3beec693bb5937dbc4fa1957a54e7660859b-1580x870.png/OpenStudio.png)

You can open any version by clicking on the overflow menu and Open in ProtoPie Studio button. You can make changes to the components inside the interaction library and publish your changes to the library as a new version.

![HowtoRestore](https://cdn.sanity.io/images/vidqzkll/production/2498bab8f5ab3964237c7a8308bbc03898366940-2370x1305.png/HowtoRestore.png)

In the same way, you can restore any previous version of an interaction library which then becomes the latest version.

[Video: Restore Version - Video](https://www.youtube.com/watch?v=iw9_vW1Rkjk)

### Archiving an Interaction Library

To archive an interaction library, click on the settings icon in the left panel and find the Archive tab. When clicking on the Archive button, the library will be archived and moved to the Archived tab.

![ArchiveLibrary](https://cdn.sanity.io/images/vidqzkll/production/65551ec5fbf562fbc672482cebe7617b53ff8d88-1580x870.png/ArchiveLibrary.png)

![ArchivedTab](https://cdn.sanity.io/images/vidqzkll/production/4be7d42415837a40160edbb4e66af727a6fde50a-1580x870.png/ArchivedTab.png)

All archived interaction libraries reside in the Archive tab. You can click on the settings icon by hovering over a library card to find the option to restore the interaction library.

[Video: Restore Archived - Video](https://www.youtube.com/watch?v=Ftjy_orMw2I)


---

---
title: "Managing Library Members"
url: https://www.protopie.io/learn/docs/interaction-libraries/managing-library-members
---

# Managing Library Members

# Managing Library Members

Team libraries only.

### Permissions

When you create a team library, you become the library owner by default. Or you can become a library owner when ownership has been transferred to you by the previous library owner.

The library owner can add and remove library members. Library members, if they are editors, can make changes and publish them to the interaction library, see the version history, and restore previous versions.

A library owner can do everything a library member can. In addition, a library owner can transfer ownership, change the information of the library, and archive libraries.

See below what the differences are between what a library owner and a library member can do when both of them are editors.

### Adding and Removing Library Members

The library owner can easily add and remove library members among members of the team.

By clicking on the + button on the left panel, you can reveal the list of library members. Then by checking or unchecking the checkboxes next to the names, the owner can add or remove library members.

[Video: Add & Remove Member - Video](https://www.youtube.com/watch?v=DnYenjiKm3k)

### Transferring Ownership

As the library owner, you can transfer the ownership to one of the library members. Click on the settings icon in the left panel in the desired team library and click on the Transfer tab in the following window. You can then select a library member in the drop-down menu. By clicking on the Transfer Ownership button, you are downgraded to a library member. There can be only one library owner per team library at a time.

[Video: Transfer Owner - Video](https://www.youtube.com/watch?v=Z0qn2U9IHow)


---

---
title: "Creating Interaction Recordings"
url: https://www.protopie.io/learn/docs/interaction-recordings/creating-interaction-recordings
---

# Creating Interaction Recordings

# Creating Interaction Recordings

![Interaction Recordings](https://cdn.sanity.io/images/vidqzkll/production/5774ba3deec6c41395ea5ab37074716215591e46-2000x1103.png/Handoff-2-2.png)

An interaction recording captures the intended scenario of interactions within a prototype, visually demonstrating their planned behavior. It includes valuable information that engineers require to implement the interactions accurately in production, including **durations**, **delays**, **easing**, and **layer** **properties**, conveniently accessible in a single overview.

Engineers can easily access the specifications of each interaction, understand its composition, and interpret its intended purpose. Learn more about how ProtoPie enables [seamless collaboration](https://www.protopie.io/blog/how-protopie-makes-collaborative-design-easy-for-engineers-&-developers) between designers and engineers.

With the Pro and Enterprise plans, editors have the freedom to create an unlimited number of interaction recordings.

## How to Create an Interaction Recording

To easily access the Handoff option within ProtoPie Studio, make sure you've enabled the Handoff shortcut in the Preferences menu.

1. Click the Handoff button in the toolbar of ProtoPie Studio.

1. Select the Record option.

1. Interact with the prototype to demonstrate the desired interactions.

1. To finish recording and save the interaction, click the Stop button at the top of the page.

1. Copy the link for the interaction recording and share it with your developers.

Another option is to create an Interaction Recording straight from the prototype's [cloud](https://www.protopie.io/learn/docs/cloud/getting-started) page. Simply click the Handoff button in the toolbar and follow the steps mentioned above.

![Interaction Recordings](https://cdn.sanity.io/images/vidqzkll/production/f62fffdaa779fd88b6f141395d11e982cc980566-2175x1200.png/Creating-interaction-recordings-2.png)


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/interaction-recordings/getting-started
---

# Getting Started

# Handoff

![interaction-recipes](https://cdn.sanity.io/images/vidqzkll/production/ebaf98a40a2fb603d4613762be482fdcdc41e4fa-2560x1440.gif/recording-interaction.gif)

The Handoff feature in ProtoPie helps bridge the gap between design and production. 

With this feature, you can [create an interaction recording](https://www.protopie.io/learn/docs/interaction-recordings/creating-interaction-recordings) that showcases user flows, element behaviors, and overall interaction integration within your prototype. The interaction recording contains specifications such as the duration, delays, and easing functions, which gives developers a clear and accurate understanding of how your interactions are intended to work.

Handoff is available to all users. Free and Basic plan members can create one interaction recording per prototype in the cloud. Users on the Pro and Enterprise plans can create unlimited interaction recordings.


---

---
title: "Managing Interaction Recordings"
url: https://www.protopie.io/learn/docs/interaction-recordings/managing-interaction-recordings
---

# Managing Interaction Recordings

# Managing Interaction Recordings

### Renaming Interaction Recordings

To rename your interaction recordings, simply follow these steps:

1. Navigate to the Recordings list.

1. Hover over the recording you wish to rename.

1. Click on the pencil icon that appears.

1. Enter a new name for the recording using up to 30 characters.

![7 recording rename](https://cdn.sanity.io/images/vidqzkll/production/9331e397cdf7dc1d40c5f97922eb1384e9d18783-1450x800.png/Renaming-interaction-recordings.png)

### Deleting Interaction Recordings

To permanently delete an interaction recording, simply follow these steps:

1. Navigate to the Recordings list.

1. Hover over the recording you wish to delete.

1. Click on the trash icon that appears.


![8 recording delete](https://cdn.sanity.io/images/vidqzkll/production/2834a905937d61b296ba24ceee117812a9c90825-1450x800.png/Deleting-interaction-recordings.png)


---

---
title: "Recording Page"
url: https://www.protopie.io/learn/docs/interaction-recordings/recording-page
---

# Recording Page

# Recording Page

The recording page provides a comprehensive view of the interaction recording, with all the necessary interaction specifications for implementation.

![recording page](https://cdn.sanity.io/images/vidqzkll/production/cb51c23ac9c1915d96e2626dc15a14e0dbc88bee-2175x1200.png/Interaction-recording-page.png)

### Timeline

To replay the recorded scenario of an interaction recording, simply click the Play button and adjust the playback speed as desired. For more precise control, you can use the timeline scrubber to navigate forward or backward to any specific point in time.

![5 recording play](https://cdn.sanity.io/images/vidqzkll/production/aec98303d6e669a8df46613a3fb5d013fee05c1b-2175x1200.png/Timeline.png)

### Interaction Specs

If you select any trigger or response on the timeline, you will see the corresponding interaction specifications and layer properties in the property panel on the right side of the page.

![6 recording focus](https://cdn.sanity.io/images/vidqzkll/production/31173ca3d910795d72d06e0a4da7f5eeb79abdd9-2175x1200.png/Interaction-recording-specs.png)

### Layer Panel

The layer panel, located on the left side, provides a visual representation of the prototype's layer structure. By selecting a specific layer in the panel, it will be highlighted in the preview area, allowing for easy navigation and identification.

### Distance Between Objects

![Distance Between Objects](https://cdn.sanity.io/images/vidqzkll/production/b8b63b26dc777ce92f2f4ff03e149daaa89ee67e-2175x1200.png/Interaction-recording-objects.png)

To check the horizontal and vertical distance between objects in the preview, simply hover your mouse over the objects of interest. The distance measurements will be displayed.

### Shortcuts

Enhance your efficiency by utilizing these handy shortcuts to control the timeline:


---

---
title: "Easing"
url: https://www.protopie.io/learn/docs/interactions/animation-curves
---

# Easing

# Easing

Enhance your animations with realistic movements using the easing features in ProtoPie.

In real life, objects don't abruptly start or stop moving. That's why it's crucial to include easing in your prototypes to achieve natural animations.

By incorporating easing functions, you can create visually captivating and engaging transitions that add a sense of realism and natural movement to your designs like in  the following example.

![bunny vs wolf game start](https://cdn.sanity.io/images/vidqzkll/production/c2b6b7677323d6eccc717bf856a5c40ea9210949-1332x998.gif/game-start-animation.gif)

Learn how easing was used in this example in our newest [Mobile Game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass).

## Standard Easing Options

### Linear

With **Linear** easing, there are no accelerations or decelerations during the animation. The object moves in a smooth and uniform manner, maintaining a steady pace throughout the transition.

### Ease

**Ease** easing is used to control the acceleration and deceleration of transitions. It adds a sense of smoothness and natural movement to objects or elements that are animated or transitioning between states.

### Ease In

**Ease In** easing is used to control the initial acceleration of transitions. It focuses on creating a gradual and gentle start to the animation, where the object or element starts moving slowly and then gains speed as the animation progresses.

### Ease Out

**Ease Out** easing is used to control the deceleration of transitions. It focuses on creating a gradual and smooth slowing down of movement as the animation comes to an end.

### Ease In Out

**Ease In Out** easing is used to create smooth and balanced transitions. It combines the characteristics of both **Ease In** and **Ease Out** easing to provide a gradual acceleration at the beginning, a consistent speed in the middle, and a gradual deceleration towards the end of the animation.

### Cubic Bezier

**Cubic Bezier** easing is used to provide precise control over the acceleration and deceleration of transitions. It allows you to define custom curves by adjusting its four points (two anchor points and two control points), offering flexibility and the ability to create unique and complex motion effects.

### Spring

**Spring** easing is used to simulate the motion of a spring. It adds a dynamic and bouncy effect to transitions, mimicking the behavior of a physical spring being stretched and released.

## Custom Easing Options

### Creating Custom Easing Presets

In ProtoPie, you have the ability to create custom easing presets. Follow these steps to create your own custom easing:

1. Choose a standard easing option from the Standard easing list.

1. Click the "+" button to add a new easing preset.

1. Modify the duration and predefined values by either entering new values or dragging the control points to your desired position.

1. Double-click above the input area to rename the easing preset.

1. The newly created easing preset will be saved in the Custom easing list, making it readily available for future use.

### Exporting & Importing Custom Easing Presets

After creating a new custom easing preset, you can choose to export it as a .json file to your local computer. This file will include all the presets currently in the Custom list. This feature enables you to effortlessly share the easing presets with your team members or keep them for future use, especially if you switch to a different device.

![Exporting & importing custom easing presets.](https://cdn.sanity.io/images/vidqzkll/production/0ef0f10c8283c9ceefd0f174183b1706f09a0be1-1087x691.gif/custom_preset.gif)


---

---
title: "Annotations"
url: https://www.protopie.io/learn/docs/interactions/annotations
---

# Annotations

# Annotations

Annotations are documentation blocks that can be placed between interaction pieces (triggers and responses) to provide context and explanations. They act as inline comments appearing directly in your interaction flow, making them ideal for:

- Documenting interaction logic for team handoffs

- Explaining complex prototype behaviors

- Providing implementation notes for developers

- Adding context for stakeholder reviews

![Annotations](https://cdn.sanity.io/images/vidqzkll/production/0afb035da53fe0b0b09c1ea25609a07483b2ec29-1920x1080.gif/Annotations1.gif)

## **Creating Annotations**

### **From the Top Bar**

Click the Annotation button in the top toolbar to add an annotation:

- **With interaction piece selected:** Creates a Trigger-level or Response-level annotation directly below the selected piece.

- **With no selection**: Creates a Trigger-level annotation at the bottom of the interaction panel.

- **With layer selected**: Deselects the layer and creates a Trigger-level annotation at the bottom.

![HoverAnnotation](https://cdn.sanity.io/images/vidqzkll/production/79e6b38cab6840f46608667735980cd9de86200f-1920x1080.gif/HoverAnnotation.gif)

## **Between Interaction Pieces**

Hover between any interaction pieces to reveal the **+** button, then select Annotation. This creates a Response-level annotation at that specific position.

![TriggerAnnotation](https://cdn.sanity.io/images/vidqzkll/production/fce07a6cb28fead469ab73af2676aa944b3b8799-1920x1080.gif/TriggerAnotation.gif)

## **Annotation Levels**

Annotations exist at two hierarchical levels.

### **Trigger Level**

Trigger-level annotations that provide general context for a set of interactions. These are created from the top bar or by dragging Response-level annotations to the trigger level.

![ResponseAnnotation](https://cdn.sanity.io/images/vidqzkll/production/715cb1f489fe3e3d9988bdd24e5f2c45b399671f-1920x1080.gif/ResponseAnnotation.gif)

### **Response Level**

Annotations nested within triggers that document specific responses or interaction sequences. Created between interaction pieces or by dragging Trigger-level annotations under a trigger.

![MoveAnnotation](https://cdn.sanity.io/images/vidqzkll/production/8d415cb196353219a8f668fbb35cfabb4ba921bc-1920x1080.gif/MoveAnnotation.gif)

**ð¡Tip:** You can easily convert between levels by dragging annotations to different positions in the interaction hierarchy. You can also use shortcuts to move them:

- To the top:

  - Mac: `]` or `â¥â ]`

  - PC: `]` or `Ctrl + Alt + ]`

- To the bottom:

  - Mac: `[` or `â¥â [`

  - PC: `[` or `Ctrl + Alt + [`

## Editing Annotations

Click on an annotation to edit its content in the property panel. Annotations support full markdown formatting, allowing you to:

- Add headers and emphasis (bold, italic)

- Create lists and tables

- Include code blocks for technical documentation

- Add links to external resources

When focused, you'll see raw markdown text. When you click away, the content renders with proper formatting.


---

---
title: "Responses"
url: https://www.protopie.io/learn/docs/interactions/responses
---

# Responses

# Responses

In ProtoPie, a Response is an interaction piece that is triggered by a [Trigger](https://release-docs.protopie.io/learn/docs/interactions/triggers). It can be described as the action initiated by the trigger to which it is tied. 

## Move

Moving a layer to specific coordinates.

## Scale

Scaling a layer up or down. 

## Rotate

Rotating a layer to specific angles.

## 3D Rotate

Rotating a layer to specific angles in a three-dimensional field.

## Opacity

Changing the transparency of a layer.

## Color

Changing the color of a layer. 

## Radius

Changing the radius of individual corners or all corners of a layer.

## Border

Adding custom borders to a layer. 

## Shadow

Adding custom shadows to a layer. 

## Background Blur

Blurring underneath layers based on specific blur effects. 

## Reorder

Changing the order of layers in a stack.

## Scroll

Scrolling to a specific position within a container.

## Jump

Going from one scene to another scene.

Use Smart Jump to animate transitions between scenes automatically. [Learn more](https://www.protopie.io/blog/animated-transitions-with-smart-jumps) about Smart Jump.

## Send

Send responses enable device interactions, but they cannot be used independently.

They must be used with Receive triggers. Such actions fire when a prototype with a Receive trigger receives a message sent from a different prototype through the Send response. The received message should always match the sent message.

Sending and receiving messages can be used within the same scene to modularize interactions or reuse a set of responses, avoiding repetitive work.

## Link

Opening websites or apps through URL schemes.

## Text

Changing the content and properties of a text layer. Text responses have no duration.

## Media

Modifying the content of an image, video, or Lottie layer. Depending on your plan, you can import images from your local files or, for Enterprise users, from a [self-hosted URL](https://www.protopie.io/learn/docs/basic-features/layers#supported-self-hosted-url-format).

The following formats are supported:

- Image: PNG, JPG, JPEG, BMP, GIF, SVG, and WebP.

- Video: MP4 (H.264), WebM, and MOV files up to 100 MB.

- Lottie: ProtoPie does not support Lottie files that use expressions.

Learn more about the [supported media files](https://www.protopie.io/learn/docs/basic-features/layers#supported-media-file-format).

## Focus

Focusing in or out of an input layer. 

## Camera

Accessing or exiting the device's native camera.

The Camera response must be used together with the camera layer. It also enables you to utilize the QR & Barcode Scanner function for scanning [QR codes](https://www.protopie.io/blog/qr-code-scanner) and barcodes directly within your prototype.  

## Playback

Playing, pausing, and seeking video, audio, and Lottie layers. 

## Volume

Controlling the volume of video or audio files.

## Vibrate

Activating vibration and haptic feedback on smart devices. 

Refer to Google'sÂ [Android Developer Documentation](https://developer.android.com/reference/android/view/HapticFeedbackConstants)Â and Apple'sÂ [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/ios/user-interaction/feedback/#haptics)Â for more information about haptic feedback.

## Speak

Activating reading a text out loud, either by inputting the text or through a [formula](https://www.protopie.io/learn/docs/formulas/getting-started).

[Learn more](https://protopie.io/learn/docs/voice-prototyping/getting-started) about voice prototyping.

## Listen

Activating listening to voice commands. 

By default, prototypes do not pick up any voice commands. Hence, listening needs to be enabled first. Prototypes can listen to voice commands continuously for up to 5 minutes.   

[Learn more](https://protopie.io/learn/docs/voice-prototyping/getting-started) about voice prototyping. 

## Reset

Resetting the current scene, a layer, or a variable. You can reset the whole scene and also default a layer or variable back to its initial state.

## Stop

Halting the animation of a layer. For example, you can use Stop to stop a loading or progress bar. 

## Assign

Overwriting the value stored in a variable. 

## Condition

Configuring parameters that need to be met to trigger responses.


---

---
title: "Timelines"
url: https://www.protopie.io/learn/docs/interactions/timelines
---

# Timelines

# Timelines

Easily manage your [responses](https://www.protopie.io/learn/docs/interactions/responses) in ProtoPie with the help of the timeline and valueline. 

These visual tools provide a clear overview of your response parameters, including duration, start delay, and mapping range. Simply hover over a response in edit mode, and a range bar will appear, allowing you to easily modify these values by dragging. It's a convenient way to fine-tune your interactions. 

ProtoPieâs timeline feature gives users granular control over game elements to achieve sequenced animations.

![bunny vs wolf game countdown](https://cdn.sanity.io/images/vidqzkll/production/45e2d8e11d3fb7883e04b69bb271969556dbde45-1331x998.gif/game-countdown-animation.gif)

Note that timelines and valuelines are **not displayed for responses connected to continuous triggers,** as these triggers are not mapped to specific time values. 

If you want to learn more about how to manage timelines to add smoothness to your animations, join the [Mobile Game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass). 

## Timeline

The timeline provides a clear visual representation of a response's time, delay, and repeat settings. 

With the timeline, you can quickly select and modify multiple responses simultaneously. For example, if you want to change the delay or duration of several responses at once, simply select them on the timeline and make the adjustments in one go.

![img timeline](https://cdn.sanity.io/images/vidqzkll/production/203e6e04ad6342bb8b129085505f5f5c9ca2fff8-976x530.png/image.png)

## Valueline

The valueline is a visual representation of a layerâs movement range, when its responses are linked to a [Chain](https://www.protopie.io/learn/docs/interactions/triggers#chain-trigger-property) trigger.

![img valueline](https://cdn.sanity.io/images/vidqzkll/production/d75f69432f06b2fa53fbab47ee1fd4dd207a5934-1260x344.png/image.png)


---

---
title: "Triggers"
url: https://www.protopie.io/learn/docs/interactions/triggers
---

# Triggers

# Triggers

In ProtoPie, a Trigger is an event that triggers specific actions, called [Responses](https://www.protopie.io/learn/docs/interactions/responses), in your prototype.

## Touch Triggers

A touch trigger involves actually touching the display of a smart device. It can be, for example, a Tap, Long Press, or Drag action. Multi-touch gestures, such as Pinch and Rotate, are also supported.

### Tap

An action where the tip of a finger touches the touchscreen and is raised immediately.

#### Trigger Property



### Double Tap

An action where the tip of a finger touches the touchscreen twice rapidly.

#### Trigger Property



### Touch Down

An action where the tip of a finger touches the touchscreen.

#### Trigger Property



### Touch Up

A response is triggered as soon as a user releases a layer. For example, it can be used in combination with drag to initiate an interaction when a user drags and releases a layer.

#### Trigger Property



### Long Press

An action where the tip of a finger is raised after a certain amount of time touching the touchscreen.

#### Trigger Properties



### Fling

A response is triggered when a layer is swiped across the chosen direction, at a speed faster than the default speed.

#### Trigger Property



### Pull

Pull is a trigger with true/false properties. If the target layer is pulled past a certain point, the layer moves according to the distance set by the user in the trigger's property panel. If the conditions arenât met, the layer returns to its original position.

#### Trigger Property



### Drag

An action where the tip of a finger moves across the screen while touching the touchscreen.



#### Trigger Property

#### The response properties linked to drag triggers



### Pinch

An action where two fingers pull away from or come toward each other while touching the touchscreen.



#### The response properties linked to pinch triggers



### Rotate

An action where two fingers turn in the same direction while touching the touchscreen.



#### The response property linked to the Rotate trigger



## Conditional Triggers

As the name implies, conditional triggers activate Interactions based on specific conditions. 

### Chain

An action where the changes of a property of one layer changes the property of another layer.



#### Trigger Property

#### Response Properties after Chain



### Range

The Range trigger fires when an objectâs property or variable transitions into a range (hence the name) you define. This trigger will only fire once as the property transitions into the range. For example, you might define a Range trigger that fires when the x property of an object becomes 200 pixels or greater. The trigger will fire once as the object transitions from 199 to 200. This wonât fire again as the x property remains 200 or greater, and it wonât fire when the property drops below 200 (e.g., 200 to 199).Â However, it will fire again if the property once again transitions from 199 to 200.



#### Trigger Properties



### Start

Start allows you to activate interactions upon loading a certain scene.



#### Trigger Properties



### Detect

A response is activated when a layer property or variable changes.



## Mouse Triggers

Mouse triggers activate based on the movement of a computer mouse. They allow you to create interactions based on the cursor hovering over or leaving an object.

### Mouse Over

A response is triggered when the mouse pointer moves over an object.



### Mouse Out

A response is triggered when the mouse pointer moves away from an object.



## Key Trigger

### Press

A response is activated when a key on a physical keyboard or an Android device is pressed.

#### Trigger Properties



## Input Triggers

The input trigger must be used with an input layer. 

### Focus

A response is activated upon an [input layer](https://www.protopie.io/learn/docs/basic-features/layers#input-layer) receiving or losing focus. A Focus In event implies that the blinking placeholder is visible in the input layer, or that the native keyboard appears if a smart device is used. A Focus Out is simply the opposite.

#### Trigger Properties



### Return

A response is activated upon pressing the return key on a physical keyboard, or a native keyboard if a smart device is used.



## Sensor Triggers

Sensor triggers enable accessing specific native sensors in smart devices and mapping responses onto their properties.

### The response properties linked to the Sensor trigger



### Tilt

A response is activated upon a smart device reaching specific tilting angles. 

#### Trigger Property



### Compass

A response is activated based on the direction the smart device is pointing towards.
For example, to create a realistic compass prototype like [this one](https://cloud.protopie.io/p/62231de961), Compass is used with the Rotate response. The movement of the needle (Angle) is then determined by the detected compass angle (Degree), a value between 0 and 360, and the set rotation direction (clockwise/ counterclockwise).



### Sound

A response is activated based on the volume of a detected sound.

Learn how to use this trigger is used in the [Mobile Game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass).



### 3D Touch

A response is activated based on the intensity of a touch force. The value of the touch force can range from 0 to 6.7. 

*Note that 3D Touch is only supported by older Apple devices such as iPhone 6s, iPhone 6s Plus, iPhone 7, iPhone 7 Plus, iPhone 8, iPhone 8 Plus, iPhone X, iPhone XS, and iPhone XS Max.*



### Proximity

It's used to create interactions based on how close or far something is from the smart device's proximity sensor.

#### Trigger Properties



### Receive

Receive triggers make interactions among devices possible. They must be used together with [Send responses](https://www.protopie.io/learn/docs/interactions/responses#send). A response is activated when a device with the Receive trigger accepts a message sent from a different device using a Send response. The message received on one device should match the one sent from the other device.

Send and Receive messages can be used within the same scene to modularize interactions or reuse a set of responses, avoiding repetitive work.



### Voice Command

The Voice Command trigger enables triggering responses based on voice commands. You can set the Voice Command trigger to be triggered either while someone is speaking or after someone finished speaking. It's possible to include or exclude specific phrases within the commands.

In order to use the Voice Command trigger, you need to enable listening using the Listen response.

[Learn more](https://protopie.io/learn/docs/voice-prototyping/getting-started) about voice prototyping.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/introducing-protopie/getting-started
---

# Getting Started

# Introducing ProtoPie

[Video: What is ProtoPie?](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DZog81HSGAU8)

It's time to make interaction design the heart of your workflow with ProtoPie! ProtoPie allows you to easily create and test tomorrow's digital experiences across a range of devices, including smartphones, desktops, TVs, and car dashboard screens. 
Get ready to unleash your creativity and bring your designs to life in a way that feels truly immersive and engaging.

Get started today for free! [**Download ProtoPie Studio here**](https://www.protopie.io/download#studio-download), available for MacOS and Windows.

The magic starts inside [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem#proto-pie-studio)âthe actual prototyping app for macOS and Windows computers. [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) allows you to test prototypes on any iOS, iPadOS & Android smartphone or tablet displays. [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/getting-started) makes sharing prototypes with stakeholders easy and fast. And if you need to prototype more advanced connected experiences, upload it all to ProtoPie Connect!

[Learn more](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem) about the ProtoPie ecosystem.

Ready to try ProtoPie? [Learn more](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype) about making your first prototype in ProtoPie.

 

## Why ProtoPie?

ProtoPie unleashes your creativity and allows you to explore a wide range of interactions, from small micro-interactions to advanced multi-screen animations. But why should you consider adding ProtoPie to your team's tool stack? Here are a few compelling reasons:

### For Anyone

- **Get something tangible in your hands.** ProtoPie lets you bring your ideas to life by creating interactive prototypes that you can touch, feel, and interact with. It's the closest you can get to experiencing your designs in action before development.

- **Test prototypes on real displays.** With ProtoPie, you can test your prototypes on various real displays, not just limited to smartphones, tablets, and computers. Explore interactions on TV screens, kiosk touch screens, smartwatches, and more.  [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started), [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/getting-started) and [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started) offer versatile options for testing across different devices.

- **Get everyone on the same page.** Say goodbye to miscommunication during the development process. ProtoPie allows you to create prototypes that look and feel like real products, ensuring everyone on your team is on the same page and understands the design vision.

- **Gain useful insights.** Conducting user testing sessions with ProtoPie helps you gather more meaningful and actionable insights. By testing realistic prototypes, you can gain valuable feedback early on, leading to informed design decisions and better user experiences.

- **Save time.** ProtoPie empowers you to iterate faster and streamline your workflow. By reducing the back-and-forth between design and development, you can accelerate the process of bringing your digital products to market.

### For You (Editor)

- **Free your ideas.** Let your design ideas flow effortlessly, fostering the development of even better concepts. With ProtoPie's great flexibility, you can prototype anything you imagine and bring your visions to life.

- **No-code, high-fidelity prototyping.** Create the most realistic interactions with ease, thanks to ProtoPie's intuitive interface. Dive into ProtoPie's [code-free conceptual model ](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#creating-your-first-interactions)and discover the endless possibilities it offers.

- **Validate ideas quickly.** ProtoPie enables you to quickly test and validate your ideas, gaining valuable insights that refine your design direction and ensure you're on the right track.

- **Convince others faster. **With a realistic prototype in hand, it becomes easier to showcase your ideas and secure buy-in from others. 

- **Work with your favorite design tools.** Whether you prefer working with Figma, Sketch, or Adobe XD, ProtoPie plays well with them all! 

- **Extend the utility of your prototypes.** A good prototype has a long lifecycle, serving as a guide and a starting point for other designers, researchers, and engineers. Maximize the value of your work and foster collaboration by sharing your prototypes as a foundation for further exploration.

### For Other Designers

- **Avoid starting from scratch.** [Components](https://www.protopie.io/learn/docs/components/getting-started) and [interaction libraries](https://www.protopie.io/learn/docs/interaction-libraries/getting-started) enable seamless collaboration among team members, making it easier to work together on the same projects.

- **Collaborate better.** Store your prototypes in a shared team space, get instant feedback and foster a collaborative environment where ideas can thrive. Dive deeper into the capabilities of the [Pro plan](https://www.protopie.io/plans/pro) to unlock advanced collaboration features.

### For Researchers

- **Get more meaningful insights during user testing.** By creating highly realistic prototypes, you can collect valuable feedback that truly reflects the user experience. Learn more about sharing prototypes for user testing & usability testing. [Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#sharing-for-usability-testing) about sharing prototypes for user testing & usability testing.

### For Engineers & Developers

- **Facilitate design hand-off**. Find all the interaction specs needed for implementation in an interaction recording. [Learn more](https://www.protopie.io/learn/docs/interaction-recordings/getting-started) about interaction recordings.

Ready to try ProtoPie? [Learn more](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype) about making your first prototype. 

## The Way You Speak

Imagine prototyping the way you speak â with ProtoPie, you can bring your ideas to life using natural language. Say goodbye to the need for learning new mental models or complex interfaces. Instead, simply use the language you already know and use every day to create interactions in ProtoPie just as you would explain them in words.

![Prototype the way you speak.](https://cdn.sanity.io/images/vidqzkll/production/96599597c8bd459b14ed949791956ec22e9781ee-1450x859.png/prototype-the-way-you-speak.png)

[Learn more](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#creating-your-first-interactions) about ProtoPie's conceptual model.

## Easy to Start

Whether you're a seasoned pro or just starting out, ProtoPie makes creating interactions a breeze. With its intuitive interface and natural language customization, you can bring your design ideas to life in a way that's as simple as crafting a sentence. The power of ProtoPie lies in its ability to let you create any interaction you can imagine, complete with logic and so much more.

![Easy to start with ProtoPie.](https://cdn.sanity.io/images/vidqzkll/production/bb0da22eaee7c5984938b0f68cfdf91537bc15e6-1450x726.png/easy-to-start.png)

[Learn more](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#2-creating-your-first-interactions) about making your first prototype.


---

---
title: "Making Your First Prototype"
url: https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype
---

# Making Your First Prototype

# Making Your First Prototype

After [installing and opening ProtoPie](https://protopie.io/download/) on your computer, you're now all set to embark on your journey of creating your very first prototype!

To kickstart the process, let's explore the essential steps:

1. [**Importing Your Designs**](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#1-importing-your-designs): Learn how to seamlessly import your designs into ProtoPie. This allows you to bring your existing assets into the prototyping environment.

1. [**Creating Interactions:**](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#2-creating-your-first-interactions) Discover the power of ProtoPie by building your first interactions. Unleash your creativity and bring your prototype to life with interactive elements and engaging user experiences.

1. [**Testing Your Prototype**](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#3-testing-what-you-made): See your prototypes in action while building them thanks to ProtoPieâs preview mode.

1. [**Sharing Your Prototype**](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#4-sharing-your-first-prototype)**: **Once you're satisfied with your creation, it's time to share your prototype with others. Explore the different sharing options available in ProtoPie to showcase your work and collect valuable feedback.

To create realistic prototypes, it's crucial to understand ProtoPie's unique conceptual model. This model forms the foundation and backbone of ProtoPie, dictating how interactions are created and implemented.

Haven't installed ProtoPie yet? [Try ProtoPie for free](https://protopie.io/download/)!

## 1. Importing Your Designs

Start with importing your designs from [Figma](https://www.figma.com/community/plugin/908870217222043020/ProtoPie-Plugin), [Sketch](https://r.protopie.io/sketch-latest-link/), or [Adobe XD](https://adobe.com/go/xd_plugins_discover_plugin?pluginId=cec71af9) into ProtoPie using their respective ProtoPie plugin.

![import](https://cdn.sanity.io/images/vidqzkll/production/fb810beecd7f9004de31e9b5c5dfdbc142ee06f5-1270x802.png/Import.png)

Import artboards or top-level frames as scenes, and objects with the same layer hierarchy, positioning, and constraints as in Figma, Sketch, and Adobe XD.

[Learn more](https://www.protopie.io/learn/docs/import/getting-started) about importing your designs.

## 2. Creating Your First Interactions

To create your first realistic interactions, it's crucial to understand ProtoPie's distinctive conceptual model. Once you've understood how it works, you simply need to assemble the appropriate components to bring your interactions to life!

### Understanding the Conceptual Model

The conceptual model serves as the foundation and backbone of ProtoPie. It's based on how objects move in the real world.

To create a prototype, you need to create interactions. To create an interaction, combine an object, a trigger, and one or multiple responses.

![Cloud light interaction following the ProtoPie conceptual model](https://cdn.sanity.io/images/vidqzkll/production/2aa10b48c53b62efd8f719339d13c18e6249b4bd-1450x700.gif/cloud_light_interaction_conceptual_model.gif)

An object in ProtoPie refers to the layer that is impacted by an action. This can occur through either a trigger or a response. The trigger serves as the action that triggers one or more responses, while the response represents the alteration or change brought about by the trigger.

![interaction_table_protopie_triggers_responses](https://cdn.sanity.io/images/vidqzkll/production/7669d93ba9eea496a2e7f2c82903519b5b08269a-1920x1080.png/interaction_table_protopie_triggers_responses.png)

This is a visual representation of ProtoPie's triggers and responses, inspired by the periodic table of elements. Each trigger and response has its own unique functions and properties.

There is a wide range of triggers and responses you can choose from. Prototyping with ProtoPie comes down to combining triggers and responsesâto create any interaction you imagine! 

Learn more about [triggers](https://www.protopie.io/learn/docs/interactions/triggers) and [responses](https://www.protopie.io/learn/docs/interactions/response).

Let's look at this example. Once you tap the green rectangle, it moves to the right. This comes down to an interaction consisting of a Tap trigger and a Move response, both assigned to the green rectangle layer.

Of course, you can create more complex interactions. It's possible to:

- Have more than one response in an interaction.

- Assign different layers to triggers and responses in a single interaction.

- Control the duration and delay of each response.

- Control layers dynamically using formulas.

- Create interactions across multiple screens and devices 

## 3. Testing What You Made

Utilize the preview window to witness your interactions come to life. This feature allows you to identify and rectify any errors in your prototype before sharing it with others.

By default, the preview window automatically updates whenever you make changes to your layers or interactions. If you prefer to have the preview window hidden by default when launching ProtoPie Studio or switching between prototypes, simply toggle it off in the Preferences menu.

Another way is to use ProtoPie Player, a free companion app to ProtoPie Studio. View, experience, and test prototypes on iOS, iPadOS, and Android seamlessly. 

[Learn more](https://www.protopie.io/learn/docs/player/getting-started) about ProtoPie Player.

## 4. Sharing Your First Prototype

Upload your prototypes to the cloud. Share their links with your stakeholders. Depending on the prototype, stakeholders can preview it on the desktop browser, mobile browser, or in ProtoPie Player.

![uploading-prototypes](https://cdn.sanity.io/images/vidqzkll/production/7afa6b7f5c0e399a3295dba9ddb755785aabcb7c-1450x826.gif/uploading-prototypes.gif)

Stakeholders can use the prototypes stored in the cloud for usability testing and share them with other stakeholders. 

Dealing with work that's sensitive? Activate password protection for your prototype. 

[Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes) about sharing prototypes.

![protopie_cloud_share_pie_page](https://cdn.sanity.io/images/vidqzkll/production/8591f2c16006077f5ebfd6c5e0aa66226d3ebc46-725x427.png/protopie_cloud_pie_page.png)

## Ready to Learn More?

Deepen your knowledge of ProtoPie with the following courses.

- [ProtoPie 101 Crash Course](https://learn.protopie.io/course/protopie-101)

- [Tips & Tricks](https://www.protopie.io/blog/category/tips-tricks)

- [ProtoPie Workshops](https://www.protopie.io/blog/previous-protopie-beginner-workshops-our-conceptual-model)

### Learning From Others

Join our communities and learn from fellow ProtoPie users. Engage, ask, and share anything that comes to mind. Find tips, tricks, and solutions that other users have shared before.

- [ProtoPioneers Community](https://community.protopie.io/home)

- [ProtoPie Users on Facebook](https://www.facebook.com/groups/ProtoPieUsers/)

- [ProtoPie YouTube channel](https://www.youtube.com/c/ProtoPie/featured)

If you're stuck with making your Pies or have a specific topic you'd like us to cover, drop us a message here: [Ask ProtoPie](https://www.protopie.io/form/ask-protopie).


---

---
title: "ProtoPie Ecosystem"
url: https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem
---

# ProtoPie Ecosystem

# The ProtoPie Ecosystem

To get the most out of ProtoPie, it's important to have a comprehensive understanding of its ecosystem, including its four main components:

- 
The magic starts inside [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface)âthe actual prototyping app for macOS and Windows computers. 

- [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) allows you to test prototypes on any iOS, iPadOS & Android smartphone, or tablet display. 

- [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/getting-started) makes collaboration and sharing prototypes with stakeholders easy and fast. 

- And if you need to prototype more advanced connected experiences, upload it all to [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started). 

## ProtoPie Studio

Create the actual prototypes in the ProtoPie Studio desktop app, available for both macOS and Windows.

![protopie-studio](https://cdn.sanity.io/images/vidqzkll/production/9b60a974e391b705fe8af84e85699187ec2a621f-3980x2422.jpg/studio.jpg)

[Learn more](https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface) about ProtoPie Studio's interface.

## ProtoPie Player

Test your prototypes on real smart devices (smartphones & tablets) using the ProtoPie Player app for iOS, iPadOS, and Android.

[Learn more](https://www.protopie.io/learn/docs/player/getting-started) about ProtoPie Player.

## ProtoPie Cloud

Upload your prototypes to ProtoPie Cloud to save them, utilize them for design hand-off, and share them with others. They can be opened and tested using any web browser.

![protopie-cloud](https://cdn.sanity.io/images/vidqzkll/production/67651409e4c21cf67fed99e46c1ed2895dcd4c11-1466x914.png/cloud.png)

[Learn more](https://www.protopie.io/learn/docs/cloud/getting-started) about ProtoPie Cloud.

### Teams & Projects 

The Pro and Enterprise plans give you access to collaborative features on ProtoPie Cloud, including [team libraries](https://release-docs.protopie.io/learn/docs/interaction-libraries/getting-started) and [dev handoff](https://release-docs.protopie.io/learn/docs/interaction-recordings/getting-started) with an unlimited number of interaction recordings. 

![team-space](https://cdn.sanity.io/images/vidqzkll/production/b835a6ea187b2ce417d14ace682c86a4dd549431-1474x916.png/projects.png)

[Learn more](https://www.protopie.io/learn/docs/teams/getting-started) about our team features.

### ProtoPie Enterprise

The Enterprise plan allows you to use all the cloud and team features in a secure and scalable environmentâa private cloud or on-premises serverâjust for your organization.

[Learn more](https://www.protopie.io/learn/docs/enterprise/getting-started) about ProtoPie Enterprise.

## ProtoPie Connect

ProtoPie Connect is an extension app available in the [Pro](https://www.protopie.io/plans/pro) and [Enterprise](https://www.protopie.io/plans/enterprise) plans. Prototype any real-world scenarios involving multiple devices, displays, hardware, and APIs seamlessly. 

![protopie-connect](https://cdn.sanity.io/images/vidqzkll/production/777fa1ca7431f356b620f7824409a7796687fa00-1475x918.png/connect.png)

[Learn more](https://www.protopie.io/learn/docs/connect/getting-started) about ProtoPie Connect.


---

---
title: "ProtoPie Studio Interface"
url: https://www.protopie.io/learn/docs/introducing-protopie/understanding-the-interface
---

# ProtoPie Studio Interface

# The ProtoPie Studio Interface

ProtoPie Studio has a straightforward interface that you can easily navigate. This page provides more details about its key components.

Are you already familiar enough with the interface? Learn more about [making your first prototype](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype)! 

## Dashboard

![dashboard inside protopie studio](https://cdn.sanity.io/images/vidqzkll/production/58a18abf7543beb7f2156049137ae2df4ba0fcaf-2000x1327.png/dashboard.png)

After logging into ProtoPie Studio, the dashboard will welcome you. You can view your recent prototypes (Pies), create new ones, and access local or cloud-based Pies.

- **Recent Pies**: Easily locate and open your recently accessed prototypes under the Recent Pies section. This allows for quick access to your ongoing projects.

  - **Delete**: If you select this option, the Pie will be permanently deleted from your computer or the cloud page.

  - **Remove from Recent**: If you wish to remove the Pie from your list of recently viewed Pies,  select the "Remove from Recent" option.

- **Open Pie**: ProtoPie Studio offers multiple ways to open your prototypes. You can open prototypes directly from the ProtoPie Cloud or access local .pie files saved on your computer. Learn more about opening [Cloud Pies](https://www.protopie.io/learn/docs/cloud/getting-started) in ProtoPie Studio.

- **New Pie**: To begin creating a new Pie, select one of the two available New Pie buttons. You can also find more information on how to [make your first prototype](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype).

## Learn

![learn tab inside protopie studio](https://cdn.sanity.io/images/vidqzkll/production/8b737f2db7cf4abcda9b65a8a780f1bd7796feb0-2000x1327.png/learn.png)

Explore the** Learn** tab in ProtoPie Studio, where you can find the best learning materials for ProtoPie. Once you log in, you'll find a lot of helpful resources to get you started on your prototyping journey, including:

- **Interaction Templates**: Open interaction templates directly in ProtoPie. See how their interactions were made, or reuse them.

- [**Prototype **](https://www.protopie.io/prototype-gallery)[**Gallery**](https://www.protopie.io/prototype-gallery): Explore and find inspiration from the prototypes created by other ProtoPie users.

- [**Quick Start Courses**](https://learn.protopie.io/course/quick-start-course): 5-7 minute tutorials on essential features to help you become a pro.

- **Tips & Tricks**: The help you need on your journey to becoming a true ProtoPie expert.

- [**Events**](https://www.protopie.io/blog/category/events): Catch up on ProtoPieâs live events. Learn best practices and industry trends from ProtoPie experts and customers.

## Support

![support tab inside protopie studio](https://cdn.sanity.io/images/vidqzkll/production/98fc897a6885cb4f5303c1814e1b6739af5a7a13-2000x1327.png/support.png)

Need help or have feedback for us? Visit our [blog](https://www.protopie.io/blog), read our dedicated [documentation](https://www.protopie.io/learn/docs/introducing-protopie/getting-started), submit or upvote [feature requests](https://protopie.canny.io/), or join our [ProtoPioneers community](https://community.protopie.io/) to learn from other ProtoPie users. 

## Prototyping in ProtoPie Studio

![understanding-the-interface](https://cdn.sanity.io/images/vidqzkll/production/a136fc17471daa56a8fbbc8884766c729b6e1fd9-4350x2400.png/understanding-the -interface.png)

Prototypes in ProtoPie Studio open as tabs, similar to pages in web browsers. This allows for effortless switching between prototypes, enabling you to work on multiple projects simultaneously.

### 1. Layer Panel

The layer panel provides an overview of all the layers within the active scene, organized based on their hierarchy. Learn more about how [scenes](https://www.protopie.io/learn/docs/basic-features/scenes) work.

Similar to your favorite design tools, you can easily perform various actions on layers within the layer panel. These include reordering, renaming, locking, unlocking, hiding, and showing layers.

When importing designs from Figma, Sketch, or Adobe XD, the layer hierarchy remains intact, preserving the structure from the original design file. Learn more about [importing](https://www.protopie.io/learn/docs/import/getting-started) your designs.

### 2. Scene Panel

By default, the scene panel is not visible. To access it,  click on the scene panel icon located on the left side of the window.

The scene panel provides an organized view of all the scenes created within your prototype. Here, you can effortlessly navigate between scenes and adjust their order as needed. Learn more about [scenes](https://www.protopie.io/learn/docs/basic-features/scenes).

### 3. Canvas

The canvas serves as the container for your active scene and its layers. Each scene is displayed individually, allowing you to focus on one at a time.

Adding layers to the canvas can be done in several ways. You have the option to import layers from your design tool, create new ones, or add them manually. [Learn more](https://learn/docs/basic-features/layers) about layers.

To navigate within the canvas, you can easily pan around by holding down the spacebar and clicking and dragging on the screen.

### 4. Property Panel

The property panel is where you can find and adjust the properties and settings of a selected scene, layer, trigger, or response.

When selecting multiple layers simultaneously, the property panel conveniently shows their shared properties all at once.

### 5. Interaction Panel

Create your interactions in the interaction panel. Start by adding a trigger and pairing it with one or multiple responses.

The interaction panel displays all the interactions in a scene as a list. Unlike the layer panel, the interaction panel does not have a hierarchical structure.

Learn more about how to [make interactions](https://www.protopie.io/learn/docs/introducing-protopie/making-your-first-prototype#creating-your-first-interactions).

### 6. Timeline

Itâs a visual representation of the duration, delay, and repeat properties of a selected response. The timeline reflects these properties as you edit them in the property panel.

Learn more about using the [timeline](https://www.protopie.io/learn/docs/interactions/timelines).

### 7. Preview Window

Use the preview window to see your interactions in action. This helps you spot any errors in your interactions before you share the prototype.

By default, the preview window updates automatically when you make changes to your layers or interactions. 

If you want to hide the preview window by default when opening ProtoPie Studio or switching between prototypes, toggle it off in Preferences.

### 8. Toolbar

The toolbar gives you quick access to frequently used actions: 

- Add [layers](https://www.protopie.io/learn/docs/basic-features/layers).

- Change the [device](https://www.protopie.io/learn/docs/basic-features/devices) of a prototype.

- Use the preview window.

- Open prototypes in [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started).

- Upload prototypes to [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/getting-started).

### 9. Component Panel

Like the scene panel, the component panel isn't visible by default. To access the component panel, click on the component panel icon on the left side of the window. It shows all the local components and interaction libraries available in your account. 

Learn more about [components](https://www.protopie.io/learn/docs/components/getting-started) and [interaction libraries](https://www.protopie.io/learn/docs/interaction-libraries/getting-started).

### 10. Variable Panel

Like the scene and component panels, the variable panel isn't visible by default. To access the variable panel, click on **Variables**. It stores all the variables used in your active scene or across your prototype's scenes. 

Learn more about [variables](https://www.protopie.io/learn/docs/variables/getting-started).

## Preferences

![preferences inside protopie studio](https://cdn.sanity.io/images/vidqzkll/production/10996465d6b77a67332aca5bd5231f11e4d249b0-2000x1307.png/preferencias.png)

### General

In this section, you can adjust the general settings of ProtoPie Studio, including language, appearance, and canvas background color. At present, ProtoPie Studio supports English, Japanese, and Chinese.

### Scene

Set the default device that will be used when you first start creating a Pie. You can either select one of the default devices from the preset list or customize your own. Learn more about the [supported devices](https://www.protopie.io/learn/docs/basic-features/devices) inside ProtoPie Studio.

### Network

The Proxy settings in ProtoPie Studio are initially set to 'No Proxy'. If your company uses a proxy server, please refer toÂ [these guidelines](https://www.protopie.io/support/questions/account-and-login/logging-in#what-should-i-do-if-my-company-is-using-a-proxy-server)Â for instructions on configuring your proxy settings to work with ProtoPie.

### Labs

Test our latest beta features by enabling them in Labs. If you have any feedback regarding the beta features, you can easily do so from within ProtoPie Studio by filling out the âReport an issueâ form.

Alternatively, you can join our [ProtoPioneers community](https://community.protopie.io/c/start-here/) and share your thoughts there. 

![submit feedback](https://cdn.sanity.io/images/vidqzkll/production/e8349a9f96868ab2fcb17a796df0a3c4b67d7ae7-2000x1103.png/feedback.png)


---

---
title: "Testing Prototypes"
url: https://www.protopie.io/learn/docs/player/getting-started
---

# Testing Prototypes

# ProtoPie Player

ProtoPie Player is a free app designed to complement ProtoPie Studio. Easily view, experience, and test prototypes on your iOS, iPadOS, or Android devices. Access prototypes stored in the cloud, save them locally, and more â from your mobile or tablet device! 

Get ProtoPie Player for iOS, iPadOS, and Android devices:

## Testing Prototypes with ProtoPie Player

If you're looking for a reliable and efficient way to preview and test your prototypes on mobile devices or tablets, ProtoPie Player is the perfect solution. Certain features such as [input layers](https://www.protopie.io/learn/docs/basic-features/layers#input-layer), sensor-based interactions, and [voice prototyping](https://www.protopie.io/learn/docs/voice-prototyping/getting-started) work seamlessly on ProtoPie Player but may not be fully supported on web browsers.

There are various methods for opening and testing prototypes (Pies) with ProtoPie Player:

- [From the Player app](https://www.protopie.io/learn/docs/player/getting-started#testing-prototypes-from-the-player-app)

  - By opening Pies stored on the cloud via the âCloudâ page inside the Player app.

  - By opening Pies locally saved in the âSavedâ page inside the Player app.

- [From ProtoPie Cloud](https://www.protopie.io/learn/docs/player/getting-started#testing-cloud-prototypes-with-proto-pie-player), by scanning the Pieâs QR code.

- [From ProtoPie Studio](https://www.protopie.io/learn/docs/player/getting-started#testing-prototypes-from-proto-pie-studio-with-proto-pie-player), by scanning the Pieâs QR code.

- By [opening the Pie link](https://www.protopie.io/learn/docs/player/getting-started#opening-prototype-links-in-proto-pie-player) on a device that has ProtoPie Player installed.

Keep reading to learn more about testing prototypes with ProtoPie Player.

## Testing Prototypes from the Player App

### Testing Prototypes Saved in ProtoPie Cloud

To view all the Pies saved on your cloud, including those in your personal and team spaces, open the "Cloud" section in the ProtoPie Player app. Ensure that youâre logged in to access the Pies.

Learn more aboutÂ [ProtoPie Cloud](https://www.protopie.io/learn/docs/cloud/getting-started)Â andÂ [teams](https://www.protopie.io/learn/docs/teams/getting-started).

### Testing Prototypes Saved Locally

If you want to test your prototypes offline with ProtoPie Player, you can save them within the app. Go to the "Saved" section in the ProtoPie Player app to access your locally saved prototypes. Learn more about how to [save prototypes locally](https://www.protopie.io/learn/docs/player/managing-prototypes#saving-prototypes-locally).

## Testing Cloud Prototypes with ProtoPie Player

To open and test prototypes saved on your cloud page using the ProtoPie Player app, follow these simple steps:

1. Open a Pie that is saved on your cloud page.

1. Click on the Share button

1. Select the QR code option.

1. Use the ProtoPie Player app to scan the QR code.

![scan a prototype qr code from protopie cloud](https://cdn.sanity.io/images/vidqzkll/production/6f93a0e5958e0e2a0eb7117b6081318542855d7b-2000x1253.png/scan qr from cloud\.png)

## Testing Prototypes from ProtoPie Studio with ProtoPie Player

To ensure a smooth testing process, you can preview Pies from ProtoPie Studio in the ProtoPie Player app.

### Connecting ProtoPie Player to ProtoPie Studio

To connect ProtoPie Player to ProtoPie Studio, there are three methods available:

1. Scanning the QR code.

1. Entering the IP address.

1. Using a USB cable.

**1. Connecting ProtoPie Player by Scanning the QR Code**

1. Ensure your computer and smart device are connected to the same WiFi network.

1. Click onÂ **Device**Â in the toolbar in ProtoPie Studio. A QR code will show.

1. Tap on theÂ **Scan QR Code**Â button in ProtoPie Player.

1. Scan the QR code.

1. Once connected, clickÂ **Run**Â in the ProtoPie Studio toolbar orÂ **Run** in ProtoPie Player. The prototype will run on your smart device.

1. Did you make any changes to your prototype? Just run the prototype again, and the changes are reflected immediately.

**2. Connecting ProtoPie Player by Entering the IP Address**

1. Ensure your computer and smart device are connected to the same WiFi network.

1. Click onÂ **Device**Â in the toolbar in ProtoPie Studio. Your IP address will show.

1. Tap onÂ **Type IP Address**Â from the dropdown menu in ProtoPie Player.

1. Enter your IP address.

1. Your device will appear underÂ **New Devices**. Click onÂ **Approve**.

1. Once connected, click Run in the ProtoPie Studio toolbar or theÂ **Run**Â icon in ProtoPie Player. The prototype will run on your smart device.

1. Did you make any changes to your prototype? Just run the prototype again, and the changes are reflected immediately.

**3. Connecting ProtoPie Player Using a USB Cable**

1. Make sure your computer and smart device are connected using a USB cable.

  1. For Android devices, enable USB debugging.

  1. For Apple devices with a Windows PC, use [iTunes](https://support.apple.com/en-gb/guide/iphone/iph875319a3a/ios).

1. A connection will be established automatically.

1. Once connected, click **Run** in the ProtoPie Studio toolbar or the ProtoPie Player **Run** icon. The prototype will run on your smart device.

1. Did you make any changes to your prototype? Just run the prototype again, and the changes are reflected immediately.

**Enabling USB Debugging on Android**

Enable USB debugging on Android using these steps.

## Opening Prototype Links in ProtoPie Player

If you have ProtoPie Player installed on your device and open a prototype link, youâll be prompted to view the prototype using ProtoPie Player.

Learn moreÂ about [uploading and sharing prototypes](https://www.protopie.io/learn/docs/cloud/getting-started) with ProtoPie Cloud.


---

---
title: "Managing Fonts"
url: https://www.protopie.io/learn/docs/player/managing-fonts
---

# Managing Fonts

# Managing Fonts

To ensure that text and input layers display properly in ProtoPie Player using non-system fonts, you must install these fonts separately on your mobile device or tablet. Once installed, the fonts will appear in the font manager in ProtoPie Player, which can be found under settings.

## Installing Fonts on iOS & iPadOS

1. Send the font to your device via any messaging app, file storage app, email, or AirDrop.

1. Open the font with ProtoPie.

1. Click on **Install** to install the font.

## Deleting fonts on iOS & iPadOS

1. Open **Font Manager**.

1. Click on **Select** in the top right corner.

1. Select the font you want to delete.

1. Click on **Delete** in the bottom right corner.

1. You will receive a prompt to **restart the Player**, after which the application will close automatically.

## Installing Fonts on Android

1. Send the font to your device via any messaging app, file storage app, or email.

1. Download the font to your Android device.

1. Open ProtoPie Player.

1. Go to **Settings**.

1. Open **Font Manager**.

1. Click on the **+** icon in the top right corner.

1. Select the font from your downloads.

1. Click on **Install** to install the font.

## Managing Custom Fonts

*Available in the Enterprise plan only.*

Users on the Enterprise plan have the ability to effortlessly share prototypes containing custom fonts with external clients, testers, and internal stakeholders. 

Currently, the custom fonts are visible only when accessing a Pie from ProtoPie Cloud, either by scanning the QR code or opening the Pie link. Make sure that the option for anyone with the link to view is enabled. Learn more about [sharing prototypes](https://www.protopie.io/learn/docs/cloud/sharing-prototypes).

If you open a prototype locally, either in ProtoPie Studio or through ProtoPie Connect, that contains a custom font, you may encounter a missing font alert.

To ensure the intended viewing experience, you have two options:

1. Install the missing font on your device.

1. Access the prototype directly from ProtoPie Cloud, either by scanning the QR code or opening the Pie link.

Important: Prior to sharing prototypes that include custom fonts, it is crucial to ensure that your organization has the legal rights to utilize and distribute the custom fonts being shared. ProtoPie cannot be held accountable for font licenses and their usage.

For detailed instructions on applying custom fonts to text layers in ProtoPie Studio, please consult the [documentation](https://www.protopie.io/learn/docs/basic-features/layers#applying-custom-fonts-to-a-text-layer).


---

---
title: "Offline Testing"
url: https://www.protopie.io/learn/docs/player/managing-prototypes
---

# Offline Testing

# Testing Prototypes Offline with ProtoPie Player

You can use ProtoPie Player to test prototypes in an offline setting.

1. Open a Pie that has been saved in ProtoPie Cloud.

1. Double-tap the screen with two fingers.

1. Select the "Make Available Offline" option.

The prototype will then be accessible under the "Available Offline" section in the Cloud. If you are not currently logged into ProtoPie Cloud, you can find this option inside the options menu located in the upper right corner of the screen.

If a prototype that was previously available offline is deleted from the cloud, it will no longer be accessible offline. However, when you have an internet connection and open a locally saved prototype in the cloud using ProtoPie Player, it will always display the latest version.

## Saving Prototypes Locally

To save opened prototypes from ProtoPie Studio,  follow these easy steps on the Player app:

1. Open the Pie in ProtoPie Studio.

1. Click on Device and run it in ProtoPie Player.

1. Double-tap the screen with two fingers.

1. Tap "Save."

1. Find your locally saved prototypes in the "Saved" section.


---

---
title: "ProtoPie Player for Wear OS"
url: https://www.protopie.io/learn/docs/player/player-for-wear-os
---

# ProtoPie Player for Wear OS

# ProtoPie Player for Wear OS

*Available in the Enterprise plan only.*

ProtoPie Player for Wear OS enhances the prototyping experience for [Enterprise plan](https://www.protopie.io/solutions/smartwatch) subscribers. It allows for a more immersive and connected smartwatch prototyping experience.

To use ProtoPie Player for Wear OS, you'll need to use it along with [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

Download ProtoPie Player for Wear OS from the smartwatch Play Store to get started.

[Video: ProtoPie Smartwatch Solution](https://www.youtube.com/watch?v=4xOYOxAa0ew)

## Connecting to ProtoPie Connect

To establish a connection between ProtoPie Player for Wear OS and ProtoPie Connect, follow these steps:

1. Ensure that both ProtoPie Player for Wear OS and ProtoPie Connect are installed on their respective devices.

1. Make sure that both devices are connected to the same network.

1. Open ProtoPie Player for Wear OS on your Wear OS smartwatch and ProtoPie Connect on your computer running ProtoPie Studio.

1. ProtoPie Player for Wear OS and ProtoPie Connect will automatically detect each other on the same network.

1. On your smartwatch, tap on "Tap to connect" to initiate the pairing process with ProtoPie Connect.

1. Open both ProtoPie Player for Wear OS and ProtoPie Connect.

1. ProtoPie Player for Wear OS and ProtoPie Connect will discover each other automatically once they are on the same network.

1. Click on "Tap to connect" for ProtoPie Player for Wear OS to pair with ProtoPie Connect.

Learn more about [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started).

## Opening Prototypes on Wear OS

1. Upload your smartwatch prototype to ProtoPie Connect. Learn how to [add prototypes to ProtoPie Connect](https://www.protopie.io/learn/docs/connect/using-protopie-connect).

1. Select the Wear OS smartwatch from the list of devices in ProtoPie Connect.

1. To restart or exit the prototype, double-tap the screen of your smartwatch. 

![open prototypes on wear os in ProtoPie Connect](https://cdn.sanity.io/images/vidqzkll/production/c6660aeec6d85f50b90ed2b0dcc1a77069142567-2184x1374.png/open-prototypes-on-wear-os.png)


---

---
title: "Access Control"
url: https://www.protopie.io/learn/docs/security/access-control
---

# Access Control

# Access Control 

Our **cloud services** are securely hosted on Amazon Web Services (**AWS**). Specifically, ProtoPie Enterprise Cloud is hosted within a private section of AWS data centers. ProtoPie Enterprise On-Premises is the only ProtoPie solution that is self-hosted on a physical server within the customer's organization.

This page provides information about our **access control** policies and procedures for *ProtoPie Enterprise Cloud* environments, including **user account management**, **authentication**, and **authorization** protocols.

## Authentication

Our *ProtoPie Enterprise Cloud* solution is managed by two administrators within our company. Administrators are assigned a **unique user ID and password**. There are no other methods of accessing data.

We use robust Security Token Services (STS), with **multifactor authentication (MFA)** for all accounts, regardless of their permission levels.

Passwords **expire** every **90 days** and must be:

- at least 8 characters long

- contain at least one uppercase letter (A-Z)

- contain at least one lowercase letter (a-z)

- contain at least one non-alphanumeric character (! @ # $ % ^ & * ( ) _ + - = { } | ')

Accounts can modify their password, but the system remembers the 10 most recent passwords for each user and **prevents reuse**. 
Passwords are **encrypted** when stored or transferred within the system to protect them from unauthorized disclosure and modification.

We allow **up to five unsuccessful login** attempts, but users who are locked out can request administrators to unlock their accounts at all times.

Concurrent logins are allowed to enable connections across devices within ProtoPie.

### Session Management

We employ **unique on-time session keys** generated by JSON Web Tokens (**JWT**) based on the user's identity assurance.

These session keys remain valid for a period of 180 days. They are encrypted and securely stored within the user's browser. Once issued by the server, these keys are stored in the cache area of each client browser, ensuring secure session management.

## Authorization

We ensure data security through the implementation of two key policies: **separation of duties** and the **least privilege access**.

To manage access control effectively, we rely on AWS Identity and Access Management (IAM), which enables **role-based access control (RBAC)** within our solution.

### Identity & Access Management

Our Identity & Access Management process follows a formal and structured approach, comprising the following steps:

1. User ID request: users initiate the process by submitting a request through the designated User ID request form.

1. Department head review: the request undergoes thorough review by the respective department head.

1. Security officer approval: the security officer carefully evaluates the request and grants approval based on established security guidelines.

1. Account creation: Upon approval, the system administrator creates the account, ensuring a smooth onboarding process.

Identity & access management **reviews** are conducted on a **monthly basis** and also take place whenever there is a change in responsibility, or when an account departs from the company.

### Remote Access

While we cannot provide a comprehensive list of accounts with authorized server access, the information can be verified using the ID management console.

Access to the enterprise environment is exclusively granted by the administrators in our Enterprise Operations division. In cases where product engineers require temporary access for troubleshooting purposes, permissions can be granted and subsequently revoked once the troubleshooting is completed.

We provide **secure remote access** to servers through **AWS SSM** (Session Manager). Access to EC2 instances is restricted to administrators within our Enterprise Operations division.

To access an EC2 instance, administrators log into the AWS management console with Multi-Factor Authentication (MFA) enabled, via SSH. All communications are **encrypted** **using TLS 1.2**.

We capture **detailed log**s that include information such as:

- Who accessed a specific EC2 instance and the timestamp of access.

- Who worked on a particular EC2 instance and the corresponding timestamp.

These logs are periodically reviewed through CloudTrail, ensuring transparency.

Network connections associated with communication sessions are automatically **terminated** after a maximum of **30 minutes of inactivity.**

To safeguard the integrity of our remote access system, administrators are not authorized to connect from smart devices such as iPads, smartphones, or PDAs.

## OnboardingÂ andÂ Offboarding

To ensure the integrity of our workforce, our HR division follows a thorough onboarding process for new employees. This includes conducting reference checks with their former coworkers and supervisors to verify their experience and educational background. However, they are unable to inquire about credit or criminal history.

In South Korea, where our company is based, conducting background screening checks can be a challenging task due to various reasons. One significant factor is the country's prohibition of using police records for criminal history checks. Moreover, data protection laws require additional consent from individuals to release such personal information. As an organization, we prioritize compliance with these rules and regulations to avoid any legal consequences.

When an employee departs from our company, our HR division promptly informs the security team of their last working day. On that designated date, the employee's account is deactivated, ensuring they no longer have access to our systems and data. Unless otherwise requested, their account will be permanently deleted after a period of two weeks.


---

---
title: "Data Transit, Storage & Backup"
url: https://www.protopie.io/learn/docs/security/data-transit-storage-and-backup
---

# Data Transit, Storage & Backup

# Data Transit, Storage & Backup

This page provides information about our **data transit, storage, and backup** protocols for ProtoPie Enterprise Cloud environments, including data storage, data in transit and at rest protection, data retention and erasure, and data loss prevention. 

## Data Storage, Backup & Export

*ProtoPie Enterprise Cloud* users are provided with a **dedicated and private cloud** environment. Their data and networks are completely isolated from other users of our solution, ensuring the highest level of confidentiality and control.

We utilize **PSQL** for data storage. This robust database management system allows us to securely store data while maintaining its accessibility and performance.

Data is stored in the geographical location chosen by the client, which includes the United States, Europe, and Asia as options.

As an additional layer of data protection, we employ the **AWS backup system.** This comprehensive solution enables us to perform full image backups, including the operating system (OS), system files, and data. We closely monitor the backup server capacity and backup execution status on a daily basis**.** Additionally, an alert notification is automatically delivered when disk capacity exceeds 80%.

To ensure the effectiveness of our data restoration processes, we conduct **regular restore tests.** These tests are performed once a year to validate that our backup systems are functioning correctly and that data can be successfully recovered in the event of a disaster or system failure.

We do not gather or generate metadata related to how your data is utilized through inspection technologies like search engines or similar tools. Your data remains confidential and solely under your control throughout your usage of our platform.

## Data In Transit

To ensure the secure transmission of data over the internet, we employ robust security measures such as **TLS 1.2** and **HTTPS encryption** protocols. These industry-standard protocols guarantee end-to-end protection for your data during transit.

As *ProtoPie Enterprise Cloud* is hosted on AWS, we rely on the advanced data protection capabilities of **AWS Backup**. All AWS backups are **encrypted** using a unique and dedicated **KMS key** associated with the backup vault.

[Learn more](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) about how AWS KMS safeguards data.

## Data At Rest

At rest, data on EC2 instances is secured using AWS encryption solutions. This involves the implementation of **AES-256 encryption**, an industry-standard encryption algorithm known for its reliability.

The encryption process takes place at the disk level within EC2 instances. AWS generates a Customer Management Key (CMK) on behalf of our company. This encryption process is fully managed and owned by AWS, ensuring the highest level of security. Access to the encryption keys is restricted to system administrators only.

AWS KMS keys can be configured to expire every 1 or 3 years, and cannot be immediately deleted. There is a mandatory wait period of 7 to 30 days before deletion. Additionally, all customer-managed KMS keys, regardless of whether the key material was imported, can be manually disabled or scheduled for deletion.

[Learn more](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) about how AWS safeguards data.

## Data Retention & Erasure

We retain the following data:

1. Email address and name for creating a member ID

1. Text and image assets used to create prototypes

There is no specific retention period, and all information is kept until the customer terminates their contract.

Our data retention and erasure procedures **comply with ISO27001 & 27701**, as well as other certificates we have obtained.
Customers' EC2 instances are permanently deleted within 2 weeks after contract termination.

Data is erased as follows: when an object is deleted from Amazon S3, removal of the mapping from the public name to the object starts immediately, and is generally processed across the distributed system within several seconds. Once the mapping is removed, there is no external access to the deleted object.


---

---
title: "Incident Response"
url: https://www.protopie.io/learn/docs/security/incident-response
---

# Incident Response

# Incident Response

This section outlines the company's **incident response plan**, including the procedures for detecting, reporting, and responding to security incidents.

## Security Incident Process

In compliance with Korean law, ProtoPie promptly reports any security incident and personal data breach to KISA (Korea Internet & Security Agency) within 24 hours. Additionally, we notify the affected customers by email.

In the event of information spillage, we place a high priority on delivering a timely response. Our aim is to address the issue **within 24 hours**, ensuring a prompt resolution.

## Audit

### Auditing and Event Logging

All events such as system logins and system changes are actively audited and logged through [**AWS CloudTrail**](https://aws.amazon.com/cloudtrail/) and **security audit logs**, which are protected from unauthorized access, modification, and deletion. However, it's important to note that the solution does not provide the capability to configure the selection of specific auditable events to be captured in the audit log.

### ReviewingÂ AuditÂ Log Events

We have a process in place to review audit logs for indications of inappropriate or unusual activity. When significant risks arise, we promptly notify our Enterprise customers.

Our information system does not currently generate an alert for audit processing failures, but relevant logs are regularly reviewed through CloudTrail.

## Data Security Architecture

Our data security architecture is designed using industry standards (e.g., CDSA, MULITSAFE, CSA Trusted Cloud Architectural Standard, FedRAMP, and CAESARS).

### **Data Integrity**

Restrictive **measures** **and monitoring mechanisms** are implemented to prevent the installation of unauthorized software on the solution-supporting system. The data labeling within the solution adheres to the **JSON data standard.**

## Mobile Device Security

Mobile device security is a top priority in our organization. We enforce **encryption** through robust technology controls, ensuring that both the entire device and sensitive data are securely encrypted. Furthermore, we actively monitor and prevent any attempts to bypass the built-in security controls on mobile devices, including jailbreaking or rooting.

It's important to note that we do not currently deploy a centralized mobile device management solution for mobile devices accessing the production environment. However, we have implemented comprehensive security measures to safeguard the integrity and confidentiality of our data.


---

---
title: "Network & ProtoPie Player App Security"
url: https://www.protopie.io/learn/docs/security/network-and-player-app-security
---

# Network & ProtoPie Player App Security

# Network & ProtoPie Player App Security

This page provides information about our **network security** protocols for ProtoPie Enterprise Cloud environments, including firewalls, intrusion prevention systems, and antivirus & malware systems.

## **Network Security Controls**

We use **WPA2 encryption** to protect the perimeter of our wireless network environment. This encryption protocol effectively safeguards against unauthorized wireless traffic.

To ensure a consistent time reference across our infrastructure, a synchronized time-service protocol like NTP (Network Time Protocol) is utilized for all systems.

Given the architecture of our Enterprise Cloud services, which utilize Docker containers and AWS's virtual network, we do not operate within a physical network environment. As a result, the following procedures are not applicable to our network security measures:

- Vulnerability/penetration network testing.

- Infrastructure vulnerability scans.

- Access to LAN/WAN/Internet provision.

## Firewalls & IPS

To fortify our network against potential vulnerabilities, we rely on the cutting-edge **Palo Alto Web Firewall**. This solution not only incorporates powerful **anti-malware** features but also boasts an intrusion prevention system (**IDS/IPS**) that diligently inspects all network traffic for threats, regardless of ports used.

By harnessing the capabilities of the Palo Alto Web Firewall, we eliminate the need for a separate malware program to be installed on our AWS EC2 instances. This firewall solution encompasses a wide array of security aspects, including:

- Perimeter and boundary security solutions to safeguard our network boundaries.

- Protection against various common attack vectors, such as Man in the Middle (MitM), Denial of Service (DoS), IP spoofing, and port scanning.

- Additional controls that enhance security measures, such as capacity management, packet analysis, and sniffing.

- Robust defense mechanisms to thwart attacks targeting our virtual infrastructure.

## Antivirus & Malware

We employ the following protection systems to safeguard against malware, phishing, and viruses:

1. **Bitdefender**: Our end-point USB control and antivirus monitoring solution, Bitdefender, actively defends against potential threats, providing comprehensive protection for our systems.

1. **Palo Alto Web Firewall:** Network traffic within our EC2 instances is routed through the Palo Alto Web Firewall. This robust firewall solution not only incorporates intrusion detection systems (IDS) but also features anti-malware mechanisms, ensuring the highest level of security for our network.

To stay ahead of emerging threats, our virus definitions undergo regular **updates every 3 hours.**

We prioritize the security of all components within our solution, including iOS, Windows, Ubuntu (Linux), and web browsers such as Internet Explorer (IE) and Safari. Through diligent **patch management**, we ensure that all security patches are applied within 60 days of their release. For critical vulnerabilities, we expedite the patch deployment process, ensuring that patches are implemented within 30 days of their release.

Our firewall configuration follows a **whitelist-based IP** and **port control** approach, ensuring that only authorized traffic is permitted.
To maintain the effectiveness of our antivirus protection, we verify that antivirus definitions are up to date on users' endpoints using the ID management console.

The disabling of security software settings on endpoints is currently not permitted. This ensures that our systems remain protected at all times.

### Penetration Tests

We conduct comprehensive penetration tests on **an annual basis** to evaluate the security of our systems and identify any potential vulnerabilities.

To further enhance the security of our solution, we conduct regular **application security scanning** prior to implementing significant changes. We give the highest priority to the findings from these scans, ensuring they are promptly addressed during the development process.

## ProtoPie Player App Security

[ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started) is a companion app to ProtoPie Studio, providing users with a seamless experience to view and test prototypes on their iOS, iPadOS, and Android devices.

The ProtoPie Player app has successfully undergone the rigorous **approval processes** of both the **Google Play Store** and the **App Store**. This ensures that the app meets the necessary security standards and adheres to the platform guidelines.

To enhance security, the ProtoPie Player requires user permission to run, ensuring that users have control over their app experience and data.

To maintain a secure mobile app environment, we conduct thorough **penetration tests** on an annual basis. These tests are designed to identify and rectify any potential bugs or vulnerabilities, ensuring that the ProtoPie Player remains reliable and secure for our users.


---

---
title: "Overview"
url: https://www.protopie.io/learn/docs/security/overview
---

# Overview

# Security Overview 

At ProtoPie, we have always been at the forefront of innovation. As more and more companies trust us to prototype their groundbreaking ideas, we recognize the paramount importance of security. Ensuring the privacy and security of your data is our utmost concern.

Explore the following topics for a comprehensive understanding of our data handling and security measures for [Enterprise](https://www.protopie.io/plans/enterprise) environments:

- [**Compliance Framework**](https://www.protopie.io/learn/docs/security/overview#compliance-framework) 
Learn about our compliance framework and its alignment with industry standards and regulations to ensure the highest  data privacy and protection level.

- [**Risk Management**](https://www.protopie.io/learn/docs/security/risk-management)** **
Discover how we proactively identify, assess, and mitigate risks to safeguard your data from potential threats and vulnerabilities.

- [**Data Transit, Storage & Backup **](https://www.protopie.io/learn/docs/security/data-transit-storage-and-backup)
Understand the measures we have in place to secure data during transit, how we store your data with integrity, and our reliable backup procedures to prevent data loss.

- [**Access Control **](https://www.protopie.io/learn/docs/security/access-control)
Explore our rigorous access control mechanisms that allow you to manage and control who can access your prototypes, ensuring confidentiality and data privacy.

- [**Network & ProtoPie Player App Security **](https://www.protopie.io/learn/docs/security/network-and-player-app-security)
Learn about the security measures implemented within our network infrastructure and ProtoPie Player app to protect against unauthorized access and ensure secure interactions.

- [**Physical Security **](https://www.protopie.io/learn/docs/security/physical-security)
Discover the stringent physical security measures we have in place to safeguard our facilities and infrastructure against unauthorized access and potential threats.

- [**Incident Report **](https://www.protopie.io/learn/docs/security/incident-response)
Stay informed on our incident response plan, including the procedures for detecting, reporting, and responding to security incidents.

### Company Information

For information about our company, such as name, address of the head office, number of employees, product offerings, and main clients portfolio, or if you have any further security-related inquiries, please feel free to [**contact us**](https://www.protopie.io/form/enterprise-plan-contact-us). We will be more than happy to assist you and provide the information you need.

To explore and experience our prototyping solution, kindly visit [our website](https://www.protopie.io/) and take the first step towards unlocking the potential of ProtoPie for your creative endeavors!

### Service Architecture

To gain a better understanding of the technical architecture of our solution, please refer to the diagram provided at this [**link**](https://drive.google.com/file/d/1yKxYtFxBnovoz7E29YNR2R4cqdHXmA0k/view?usp=sharing). The diagram visually represents our solution's structure and components, helping you grasp the overall framework.

Regarding coding technologies, we utilize **Clojure** for the backend side and **JavaScript** for the front-end side. By leveraging the strengths of Clojure and JavaScript, we can provide a solid foundation for our solution's functionality and user interface, resulting in a secure and dynamic experience for our users.

## Keeping Your Work Secure

First and foremost, uploading prototypes to ProtoPie Cloud is optional. By subscribing to our Pro or Enterprise plans, you can easily store prototypes on your local machine.   

### Privacy Protection

*ProtoPie Enterprise Cloud* users are provided with a **dedicated and private cloud** environment. Their data and networks are completely isolated from other users of our solution, ensuring the highest level of confidentiality and control.

We also have a dedicated Data Protection Officer (DPO) who is responsible for ensuring compliance with data protection laws and regulations. The DPO oversees our data protection practices, acts as a point of contact for personal data and privacy concerns, and ensures that we uphold the highest privacy protection standards.

To understand how we handle data mapping in our database, including the identification of database fields, their purpose for collection and processing, and their retention, please refer to [our privacy policy.](https://www.protopie.io/legal/privacy-policy)

### **Managing Access to Prototypes**

At ProtoPie, we understand the importance of maintaining control over your prototypes and ensuring that only authorized individuals can access them.

Prototype owners have the flexibility to **choose the level of access** they want to grant. You can opt to allow unrestricted access, making your prototypes available to anyone with the appropriate link. Alternatively, you can restrict access to selected accounts only. For an added layer of security, we also offer password protection. With this feature, you can securely share your prototypes with external parties by providing them with a password. [**
Learn more**](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#managing-access)Â about how to manage access to prototypes.

### **Restricting Public Access to Prototypes**

With our Enterprise plan, the service admin has the capability to** manage public access**, providing you with full control over who can view and interact with your prototypes.

By restricting public access, editors within your organization can ensure that their prototypes are only accessible to individuals within the ProtoPie Enterprise environment. This means that the sensitive information contained within your prototypes remains protected from unauthorized access.[**
Learn more**](https://protopie.io/learn/docs/enterprise/service-admin#restricting-public-access-to-prototypes)Â about how to restrict public access to prototypes.

### **Role-Based Access Control (RBAC)**

With ProtoPie's Pro and Enterprise plans, we offer advanced access control capabilities through Role-Based Access Control (RBAC). RBAC allows you to have fine-grained **control over the permissions and privileges** of team members within your organization.

You can assign specific roles to team members, such as editors or viewers, based on their responsibilities and requirements. This ensures that each team member has the appropriate level of access to the cloud environment. These roles can be revoked as needed, enabling efficient management of access rights.
Learn more about [editors & viewers](https://www.protopie.io/learn/docs/teams/editors-and-viewers), [team owners & team admins](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin), and [service admin](https://www.protopie.io/learn/docs/enterprise/service-admin).

### Single Sign-On (SSO)

SSO is supported for companies on our Enterprise plan. The service admin is responsible for [configuring SSO](https://www.protopie.io/learn/docs/enterprise/single-sign-on) for the enterprise environment. With SSO, accounts can access the enterprise space through the chosen authentication solution (e.g., Okta, Auth0, OneLogin).

These two SSO protocols are supported:

- **SAML 2.0**

- **OpenID Connect** (OIDC) â on top of OAuth 2.0

[Learn more](https://www.protopie.io/learn/docs/enterprise/single-sign-on) about how to configure SSO in your enterprise environment. 

## Compliance Framework

ProtoPie operates within a stringent compliance framework to ensure adherence to relevant regulations, industry standards, and best practices. This framework serves as a guide for our operations, enabling us to maintain the highest level of legal and ethical conduct.

We are proud to hold **ISO 27001** and **ISO 27701** certificates, which demonstrate our commitment to information security and privacy management.

To verify the validity and status of our certifications, you can easily visit our protected website at [**trust.protopie.support**](https://trust.protopie.support/) for the most up-to-date information.

You will find the latest details about our certifications, including:

- ISO/IEC 27001: **2013**

- ISO/IEC 27701: **2019**

### **ISO 27001**

ISO 27001 is a widely recognized information security standard that sets the requirements for implementing an Information Security Management System (ISMS). By adhering to ISO 27001, we demonstrate our commitment to safeguarding your data and mitigating information security risks.

### ISO 27701

ISO 27701 is an extension to ISO 27001 that specifically addresses data privacy management. By aligning with ISO 27701, we demonstrate our dedication to protecting your personal and sensitive information, enhancing transparency, and complying with applicable data protection regulations.

### General Data Protection Regulation (GDPR)

ProtoPie fully complies with the General Data Protection Regulation (GDPR). The GDPR grants European Union citizens greater control over their personal data. We are committed to safeguarding your personal data, ensuring your rights to privacy and transparency.

### California Consumer Privacy Act (CCPA)

ProtoPie also complies with the California Consumer Privacy Act (CCPA), which governs the handling of personal data of California residents. The CCPA empowers you to have a say in how your personal data is used and shared. We are committed to fulfilling our obligations under the CCPA and protecting your privacy.

### Payment Card Industry Data Security Standard (PCI DSS)

While we do not process or store payment data ourselves, we work with trusted payment providers who comply with the Payment Card Industry Data Security Standard (PCI DSS). Our primary payment providers, [FastSpring](https://fastspring.com/risk-management-and-compliance/) and [Paddle](https://security.paddle.com/), as well as our secondary payment provider, [PayPal](https://www.paypal.com/c2/webapps/mpp/pci-compliance), adhere to the rigorous security requirements of PCI DSS. This ensures that your payment information is handled with the highest level of security and confidentiality.


---

---
title: "Physical Security"
url: https://www.protopie.io/learn/docs/security/physical-security
---

# Physical Security

# Physical Security

This page provides information about our **physical security controls **for ProtoPie Enterprise Cloud environments, including data access & monitoring, OS hardening, supplier management, and vendor assessment.

## Data Access & Monitoring

### Data Access

The system administrators (Enterprise Operations division) have access to the data through customer systems, including access to the hypervisors when dealing with Virtual Machine (VM) instances.

Access to information security management systems, including hypervisors, firewalls, vulnerability scanners, network sniffers, and APIs, is restricted, logged, and monitored.

### Personnel Access

Personnel access to hypervisor management functions and administrative consoles for systems hosting virtualized systems is carefully restricted, following the principle of **least privilege**.

To ensure strong access controls, we employ various technical measures, including two-factor authentication, audit trails, IP address filtering, firewalls, and TLS-encapsulated communications.

For added security, we manage removable media usage through the implementation of the [Bitdefender](https://www.bitdefender.com/solutions/free.html) solution. This helps us enforce necessary restrictions and safeguards to protect against unauthorized data transfers and potential threats.

### OS Hardening

For optimal security and to align with our recommended best practices, we suggest implementing the following technical controls to harden your operating systems and meet your business needs:

- Enable the firewall to enhance network protection.

- Regularly back up your Mac using reliable cloud storage solutions like Google Drive.

- Disable remote access to mitigate potential vulnerabilities.

- Encrypt your hard drive to safeguard sensitive data from unauthorized access.

- Install and enable antivirus protection tools, such as Bitdefender, to defend against malware and other threats.

- Configure a password-protected screensaver to prevent unauthorized access to your system.

- Disable automatic login to strengthen authentication security.

- Create a separate non-administrator account for daily use to minimize the impact of potential security breaches.

- Utilize a password manager to generate and securely store strong passwords for all your accounts.

- Disable Spotlight suggestions to enhance privacy and prevent possible information leakage.

- Ensure automatic updates are enabled to receive the latest security patches and bug fixes, keeping your system up-to-date and resilient against emerging threats.

By adhering to these recommended measures, you can bolster the security of your operating systems and ensure they effectively meet your business requirements.

## Supplier Management

### Supplier Management Controls

ProtoPie has implemented controls for managing its cloud services supplier, Amazon Web Services (AWS). We have established terms and conditions to access, process, store, or transmit organizational information using supplier systems. As such, we periodically conduct audits and request System Organization Control (SOC) reports for our suppliers.

For more information on the AWS privacy practices, visit the Amazon Web Services Data Privacy [page](https://aws.amazon.com/compliance/data-privacy-faq/).

### Performance Monitoring

In addition to conducting audits and SOC reports, we also monitor the performance of our suppliers to ensure the security and availability of customer data. As the leading cloud hosting provider, Amazon Web Services (AWS) offers extensive performance and security information on its website, enabling effortless monitoring.

### Vendor Assessment

ProtoPie conducts a cloud-hosting vendor assessment process once a year, thoroughly reviewed by our dedicated security team. Detailed information about the AWS compliance programs can be found at the following link: [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

### Outsourcing Monitoring

Given that all ProtoPie products are developed in-house, without the involvement of subcontractors or outsourced software development, there is no need for specific controls to detect source code security defects in relation to outsourced activities.


---

---
title: "Risk Management"
url: https://www.protopie.io/learn/docs/security/risk-management
---

# Risk Management

# Risk Management

This page provides information about our risk management procedures for ProtoPie Enterprise Cloud environments, including the **identification and assessment of risks,** and the **implementation of controls to mitigate** those risks.

We employ a comprehensive risk management methodology that includes the following steps:

1. **Identify** - Identify the potential risks associated with the relevant category.

1. **Assess** - Assess each identified risk in terms of potential impact, severity, and likelihood to help us understand the level of risk and prioritize our actions accordingly.

1. **Implement** - Implement reactive measures to control and mitigate disruptions caused by these risks.

## Risks Identification & Assessment

### Service Outages Risks

To ensure uninterrupted service, we rely on AWS's world-class data centers, which are designed with robust security measures and redundancies to mitigate the risks of utility service outages, such as power failures and network disruptions.

Here are some key security measures implemented in AWS's data centers:

- **Emergency Power Shutoffs**: AWS's data centers have emergency power shutoffs located in easily accessible areas. These shutoffs are protected from unauthorized activation, ensuring that only authorized personnel can initiate emergency power procedures.

- **Uninterruptible Power Supply (UPS)**: To seamlessly handle power source loss, AWS's data centers utilize short-term UPS systems. These systems provide temporary power to facilitate a smooth transition to alternate power sources, ensuring continuous operation of the information system.

- **Water Leakage Protection**: Measures are in place to protect the information system from damage caused by water leakage. AWS's data centers employ master shutoff or isolation valves that are easily accessible, properly functioning, and known to key personnel. These valves help prevent water-related incidents from impacting the system's integrity.

- **Fire Suppression and Detection**: AWS's data centers are equipped with fire suppression and detection devices/systems supported by independent energy sources. This ensures rapid response and effective containment in case of a fire emergency, minimizing potential damage to the infrastructure.

- **Temperature and Humidity Control**: Regular monitoring and maintenance of temperature and humidity levels are conducted in AWS's data centers. These measures ensure that the environmental conditions are kept within acceptable ranges to safeguard the equipment and maintain optimal performance.

### High-Impact Environmental Risks

To ensure the safety and integrity of your data, we utilize data centers provided by AWS, strategically located in areas that offer world-class safety and resilience against environmental threats such as floods, tornadoes, earthquakes, and hurricanes.

Customers have the option to choose the geographical location where data are stored, although itâs primarily based on the location of the company that owns the data in compliance with the Data Process Agreement (DPA).

### Threat Vectors Management

To effectively manage the main threat vectors for our service, we have implemented comprehensive measures:

- **Continuous Monitoring**: Our networks and systems are continuously monitored using advanced tools such as firewalls, and AWS Security Manager. We proactively review monitor logs to identify any suspicious activities or potential threats, allowing us to take prompt action and maintain a secure environment.

- **Penetration Testing**: To identify vulnerabilities and enhance our security measures, we conduct annual penetration tests. These tests help us identify potential weaknesses in our systems and applications, enabling us to address them proactively and fortify our defenses.

- **ISO27001 and 27701 Audits**: We undergo annual audits for ISO27001 and 27701 compliance. These audits ensure that we adhere to internationally recognized standards for information security management and privacy practices.

- **Personal Information Protection**: While we currently do not have specific cyber security insurance, we are committed to adhering to the guidelines set forth by the Personal Information Protection Act in Korea. As part of our efforts to mitigate risks associated with protecting personal information, we have subscribed to a personal information protection liability insurance policy provided by KB Insurance. This coverage helps mitigate potential risks associated with the protection of personal information.

## Business Continuity

Business continuity is an integral part of our operations, ensuring that we have the capacity to sustain vital functions even in the event of a disaster. Our risk management practices and protocols are designed to prevent interruptions to essential services and enable a swift and seamless recovery, allowing us to restore full functionality as quickly as possible.

### Business Continuity Planning (BCP)

We conduct a thorough BCP test **once a year** to evaluate the effectiveness of our plan and identify areas that may require improvement. This testing process allows us to assess our readiness in the event of a disruption or disaster and ensures that our organization can continue essential functions without major interruptions.

In addition to BCP testing, we also conduct regular tests of our **backup and redundancy mechanisms**. These tests, performed **annually**, are designed to verify the reliability and functionality of our backup systems.

By testing these mechanisms, we can confidently rely on them to restore data and services in case of any unforeseen incidents or system failures.

### Contingency Plan Development

As part of our commitment to ensuring business continuity, we have developed a comprehensive contingency plan for our information system. This plan outlines the steps and procedures to be followed in the event of disruptions or incidents that may impact our operations. It serves as a roadmap for a swift recovery and helps us minimize the impact on our business and customers.

Our Business Continuity Planning and Disaster Recovery Procedures **(DRP)** are in place to mitigate risks and maintain the availability of critical services.

We prioritize the implementation of controls to ensure information security awareness among both our organization and **third-party resources** supporting our solution.

### Security Awareness Training

Our employees and contractors undergo **IT Security Awareness Training and Personal Information Training** as part of their induction process. This training equips them with the necessary skills and knowledge to effectively respond to disruptions and ensure business continuity. It covers various crucial aspects such as:

- Importance of Security Awareness

- Protect Your Operation System & Internet Transaction

- Password Security

- Email Security & Best Practices

- Backup Important Information

- Mobile Security

- Physical Security

- Social Engineering

- How to manage the risks of removable media

- Cyber Incident Reporting

Training sessions for all system administrators who have access to our solution are performed **annually** to reinforce the knowledge and practices necessary to mitigate security risks effectively.

We also provide refresher training when required to keep our personnel prepared and up to date with the latest procedures and protocols.

### Data Recovery

Our cloud solution is equipped with software and provider-independent capabilities for restoring and recovering data. We consistently evaluate and improve our practices to enhance our business recovery process.

For different levels of failure scenarios, we can commit to the following Recovery Time Objectives (RTO) and Recovery Point Objectives (RPO):

- Level 1 failure: RTO is within 6 hours, and RPO is under 6 hours.

- Level 2 failure: RTO is within 24 hours, and RPO is under 24 hours.

- Level 3 failure: RTO is within 48 hours, and RPO is less than 3 days.

### Virtual Infrastructure Capabilities

Customers have the option to download and transfer virtual machine images to another cloud provider, although there may be certain limitations. However, replicating machine images to the customer's own off-site storage location is not permitted or supported. Additionally, we offer customers the capability to undo any changes or modifications made to the virtual machine, providing them with flexibility and control over their environment.


---

---
title: "Editors & Viewers"
url: https://www.protopie.io/learn/docs/teams/editors-and-viewers
---

# Editors & Viewers

# Editors & Viewers

In a ProtoPie team, members can have either the *editor *or *viewer* role.



- **Viewers** have access to the projects and prototypes stored within their team space. They can also leave comments on prototype pages to provide feedback.

![viewer role](https://cdn.sanity.io/images/vidqzkll/production/63c8cb47a85a4984038a9586d7d540ad4d6fcf43-2888x1756.png/viewer-2 (1).png)



- **Editors** have additional privileges. They can create prototypes in [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem#proto-pie-studio), upload them to the cloud, utilize [team libraries](https://www.protopie.io/learn/docs/interaction-libraries/getting-started) for streamlined collaboration, create interaction recordings to facilitate [handoff](https://www.protopie.io/learn/docs/interaction-recordings/creating-interaction-recordings), and utilize [ProtoPie Connect](https://release-docs.protopie.io/learn/docs/connect/getting-started).

![editors in protopie](https://cdn.sanity.io/images/vidqzkll/production/99be453b3bb16f6360e88a0a4f32130871cfebd1-2886x1760.png/editors (1).png)

## Editors & Viewers Permission Levels


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/teams/getting-started
---

# Getting Started

# Teams

The [Pro](https://www.protopie.io/plans/pro) and [Enterprise](https://www.protopie.io/plans/enterprise) plans come with powerful team features that make collaboration easier.

Each team member is assigned one of the following roles: team owner, team admin, editor, or viewer.

Based on their assigned roles, team members can create and upload prototypes to the team space and manage access to prototypes, projects, and team libraries to ensure smooth collaboration.

Check out our dedicated documentation to learn more about the [differences between a team owner and a team admin](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin) or between an [editor and a viewer](https://www.protopie.io/learn/docs/teams/editors-and-viewers). 

If your team is already created and you're ready to onboard it, learn more about [onboarding your team](https://www.protopie.io/learn/docs/teams/onboarding-your-team).

## Creating a New Team

![creating-a-team](https://cdn.sanity.io/images/vidqzkll/production/ebbb6f925ead0044de04060ae57b137f6e3a9605-1532x904.gif/creating a new team in protopie.gif)

1. Log intoÂ [ProtoPie Cloud](http://cloud.protopie.io/) with your ProtoPie account.

1. Click on the **Team Space** menu in the left sidebar.

1. Click on **Create New Team**.

1. Enter a team name and click onÂ **Create**.

1. Click on **Learn more** to activate your Pro plan and unlock Pro features.

1. Choose between the yearly and monthly Pro plans.

1. Adjust the number of editor seats. 

1. Click on **Subscribe Now** and follow the checkout steps.

## Getting Started with Team Settings

![Getting Started with Team Settings](https://cdn.sanity.io/images/vidqzkll/production/04517e38ca5eb09f1d87638f9f8861834118c2a6-1152x648.gif/Getting Started with Team Settings.gif)

1. Log into [**ProtoPie Cloud**](https://cloud.protopie.io/) with your ProtoPie account.

1. In the left sidebar, click on the **Team space dropdown menu**.

1. Select the **Team Space** you want to access.

1. Click on **Team settings**.

1. In the **General** tab, you can find your **Team Id**.

1. You can also update your **Team name** and **Team logo** from this page.

## Managing Members & Roles

To invite members to a team space, open **Team settings** and click on **Members**. Then, select "Invite new member" and enter their email address.

Only the team owner and team admin/s can invite new members to the team. Invited members will receive an email invitation to join the team space.



To change a member's role, click the arrow next to their role under **Role** and select the desired role from the dropdown menu. [Learn more](https://www.protopie.io/learn/docs/teams/editors-and-viewers) about member roles.

![changing members roles in a ProtoPie team ](https://cdn.sanity.io/images/vidqzkll/production/7756eaa175547cefea5531fae44f263dfdfba70a-2621x1568.png/change_roles_protopie.png)

## Member Types & Roles

### Team Owner & Team Admin

The team owner role is automatically assigned to the account that creates and activates the team. If you need to transfer your team's ownership to another account, please [contact support.](https://www.protopie.io/form/contact-us) 

A team can have one or multiple team admins. Both the team owner and team admin can invite new members to the team and assign roles. The team owner can manage billing information and access all invoices.

[ Learn more](https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin) about team owner & team admin.

### Editors & Viewers

Viewers can be added without limit since they are free of charge. However, the number of editors you can have is determined by the available editor seats in your paid plan. 

Editors can create prototypes and upload them to the cloud, while viewers can only see the prototypes stored in their team space and leave comments.[ Learn more](https://www.protopie.io/learn/docs/teams/editors-and-viewers) about editors & viewers.

## Spaces

Team members have access to two different spaces in their account:* personal space *and *team space*.

### Personal Space

Your personal space is a private area on the cloud where you can store and manage your personal prototypes and libraries without anyone else accessing them. You can move a prototype from your personal space to a project in a team space, but you cannot move prototypes from a team space to your personal space.

Learn more about [duplicating & moving prototypes](https://www.protopie.io/learn/docs/cloud/managing-prototypes#duplicating-moving).

![personal-space](https://cdn.sanity.io/images/vidqzkll/production/12ce152c9d644f7691851e792907f2a3f1ae022f-2175x1200.png/personal-space.png)

### Team Space

Each team you join has its own space in your cloud space, so if you join three teams, you'll have three spaces.

The team space consists of all the projects created by team members, whether public or private. It also includes [team libraries](https://www.protopie.io/learn/docs/interaction-libraries/getting-started). Learn more about [projects](https://www.protopie.io/learn/docs/teams/projects).

Only editors with access to the project can duplicate or move its prototypes. Duplicates are always created within the same project as the original prototype. It is possible to move prototypes across projects within a single team space but not between team spaces. 

![team-space](https://cdn.sanity.io/images/vidqzkll/production/6c8650498794eb8cacc1e24c8a7bf68c4eaa5414-2175x1200.png/team-space.png)


---

---
title: "Onboarding Your Team"
url: https://www.protopie.io/learn/docs/teams/onboarding-your-team
---

# Onboarding Your Team

# Onboarding Your Team

You have been advocating for ProtoPie in your company, and your team has recently subscribed to the Pro plan.

Introducing a new tool or switching to new software can be challenging and sensitive. Use this guide to onboard your team efficiently.  

If you haven't created your team space yet, click [here](https://www.protopie.io/learn/docs/teams/getting-started#creating-a-team) to learn more about how to create one. If you need to add new members first, you can also [learn more](https://www.protopie.io/learn/docs/teams/getting-started#inviting-new-members) about how to do so. 

## 1. Creating a Shared Understanding

Adopting new tools in a design team can be challenging. Chances are, you've been through this process several times before.

Before introducing ProtoPie to your team, make sure everyone is on the same page. Help them understand:

- What is ProtoPie, and what does it do?

- How can ProtoPie benefit you?

- How can ProtoPie help you perform better?

- Why did you choose ProtoPie?

This [prototype](https://cloud.protopie.io/p/b498ca9a5a?ui=false&scaleToFit=true&enableHotspotHints=true&cursorType=touch&mockup=false&bgColor=%23F5F5F5&playSpeed=1&playerAppPopup=true) will help your team quickly visualize how ProtoPie can elevate their workflow.

The more shared understanding your team has, the better equipped they will be to adopt ProtoPie!

## 2. Learning Together 

Everyone is busy and has their own preferred learning style. However, here are some effective suggestions for speeding up learning within your team:

- Share **prototype examples** demonstrating the type of interactions your team usually works on. This way, your team can discover faster how ProtoPie can benefit your workflow.

- Organize **internal workshops** to train your team on using ProtoPie effectively. Workshops are an excellent opportunity to encourage dialogue, address any questions, and demonstrate how ProtoPie can add value to your projects. 

If your team members prefer to learn independently, encourage them to watch the free courses available on [ProtoPie School](https://learn.protopie.io): 

### ProtoPie 101 Course on ProtoPie School

The** **[**ProtoPie 101 Crash Course**](https://r.protopie.io/learn/course/protopie-101/) on ProtoPie School covers everything your team needs to start creating high-fidelity prototypes using ProtoPie's [**Studio, Player and Cloud**](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem).

![ProtoPie 101 course ](https://cdn.sanity.io/images/vidqzkll/production/e286c79b858d4c4b6b1e4e18044a42becea0660c-3840x2160.png/ProtoPie 101.png)

This course is perfect for those who want to start with the basics and gradually progress to key features at their own pace.

### ProtoPie Connect Course on ProtoPie School

The [**Connect Course**](https://r.protopie.io/learn/course/protopie-connect/) on ProtoPie School teaches you how to bring connected, multi-screen experiences to life using [**ProtoPie Connect**](https://www.protopie.io/learn/docs/connect/getting-started).

![ProtoPie Connect course](https://cdn.sanity.io/images/vidqzkll/production/c28cca224b1525c6e38b11ea5a09f086bb931caa-3840x2160.png/Complete Guide to ProtoPie Connect.png)

Encourage your team members to take this course if you need to create prototypes that span multiple screens, devices, and custom displays and require integration with hardware and APIs.

### Masterclass Course on ProtoPie School

Take your teamâs prototyping skills to theÂ nextÂ level with the Masterclass Course on [ProtoPie School](https://learn.protopie.io).

![ProtoPie masterclass course ](https://cdn.sanity.io/images/vidqzkll/production/b2716527a08c8e4ebbfb8a55cd3317257aae289c-3840x2160.png/Masterclass.png)

Led by ProtoPie expert Jeffrey Clarke, this course teaches how to efficiently build large-scale projects and create multi-screen experiences using ProtoPie's advanced features.

### Learning From Others

Join our communities and learn from fellow ProtoPie users. Engage, ask questions, and share anything that comes to mind. Find tips, tricks, and solutions that other users have shared before.

- [ProtoPioneers Community](https://community.protopie.io/home)

- [ProtoPie YouTube channel](https://www.youtube.com/c/ProtoPie/featured)

## 3. Reusing Interactions

The prototypes you have been creating are most likely useful for your team. Encourage them to reuse your interactions for their prototypes. 

### Example Prototypes

To help your team become familiar with ProtoPie faster, share your example prototypes in a public project in your team space. This dedicated project will enable them to analyze, learn from, and effectively reuse those prototypes.

### Components & Team Libraries

Design teams often need to reuse specific interactions across their prototypes. Creating reusable components can save time and effort!Â [Learn more](https://www.protopie.io/learn/docs/components/getting-started)Â about components.

Components can be brought together in team libraries. These libraries are collections of components your team can access and use in their prototypes. [Learn more](https://www.protopie.io/learn/docs/interaction-libraries/getting-started) about how to create team libraries.

## 4. Bringing ProtoPie into the Workflow

Your workflow involves stakeholders beyond the design team, including engineers, product managers, and researchers. They all use your prototypes in different ways and for specific purposes.

Make sure that these stakeholders can also benefit from your team's prototypes.

### Sharing & Testing

Upload your prototypes to the cloud and share the link with stakeholders. Depending on the prototype, stakeholders can test it on a desktop or mobile browserÂ or using [ProtoPie Player](https://www.protopie.io/learn/docs/player/getting-started). In the desktop browser, they can even leave comments to give you feedback.

Stakeholders can use cloud prototypes for usability testing and share their links with other stakeholders. If you're dealing with sensitive work, you can activate password protection for your prototype or use expiring links. [Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#password-protection) about configuring password protection and expiring links on ProtoPie Cloud.

### Handing Off Interactions Specs

To provide engineers with all the information they need for development, create an interaction recording of your prototype. This recording includes all interaction specifications, such as duration, delay, and easing.

[Learn more](https://www.protopie.io/learn/docs/interaction-recipes/getting-started)Â about how to create interaction recordings.


---

---
title: "Projects"
url: https://www.protopie.io/learn/docs/teams/projects
---

# Projects

# Projects

Projects allow teams to organize prototypes more effectively within a team space.

Open "Projects" to get an overview of all public projects created in your team space, as well as the private projects you are a member of.

There are two types of projects: *public* and *private*.

- Public projects:

  - All team members have access.

  - Can be converted to a private project.

- Private projects:

  - Only project members have access.

  - Cannot be converted to a public project.

## Creating Projects

Any team member can create projects. However, only editors can upload prototypes to a project. [Learn more](https://www.protopie.io/learn/docs/teams/editors-and-viewers) about editors & viewers.

![creating-projects](https://cdn.sanity.io/images/vidqzkll/production/a73bc10b736e96e7ffebedadf6f0f1aa846a9147-1294x802.gif/create new project.gif)

1. To create a project in your team space, follow these steps:

1. Click on **Create Project**.

1. Choose whether to make the project private or public. Keep in mind that once a project is set to private, it cannot be reverted back to public.

1. Enter a title and brief description for the project.

1. Click on **Create**.

## Managing Projects

The person who creates the project becomes the project owner and manages its settings. This includes tasks such as changing the name and description, transferring ownership, and archiving the project. Only the project owner can convert a public project to a private one.

![managing-projects](https://cdn.sanity.io/images/vidqzkll/production/1d071219f8528d90f833438c4c17cbf2c62219c7-725x368.png/manage projects.png)

### Managing Members in a Private Project

Only selected members, known as project members, have access to a private project.

To add or remove members from a private project, follow these steps:

1. Click on the **+** icon.

1. Add or remove members as needed.

![managing_members_in_private_project](https://cdn.sanity.io/images/vidqzkll/production/5a6122d9e505c54586250c3fb8fc6956aab2b994-1534x956.gif/manage project members.gif)

## Active & Archived Projects

A project can have one of two statuses: *active* or *archived*.

### Active Projects

The **Active** tab displays all currently active projects. All team members have access to prototypes in these projects, but only editors can upload prototypes to them.

![active-projects](https://cdn.sanity.io/images/vidqzkll/production/13bee3b7265c4c1a02b4b35321574b5a5ad05360-2175x831.png/active-projects.png)

### Archived Projects

Team members can archive projects they no longer need. All archived projects can be found under the **Archived** tab. Prototypes in archived projects cannot be accessed, and editors cannot upload prototypes to them. To make an archived project active again, restore it.


---

---
title: "Team Owner & Team Admin"
url: https://www.protopie.io/learn/docs/teams/team-owner-and-team-admin
---

# Team Owner & Team Admin

# Team Owner & Team Admin

A ProtoPie team has three types of members: **team owner**, **team admin**, and **member**.

- A team can only have one owner, but it can have multiple team admins.

- Both the team owner and team admins have the ability to invite new members and manage their roles. However, only the team owner can manage billing and delete the team.

- Members who do not hold either of these two roles are considered "regular" members.

## Managing Members

In the **Members** section of the **Team settings** page, team owners and admins have the ability to invite individuals to join the team as either [viewers or editors](https://www.protopie.io/learn/docs/teams/editors-and-viewers), as well as remove members from the team.

### Inviting New Members

1. Click on **Invite new members**.

1. Enter the email addresses of the people you want to invite (Press Enter or add a comma to activate the invite button).

1. Click on **Invite**.

1. If the invitee already has a ProtoPie account, they will become a member of the team right away. Otherwise, they will appear under **Pending** until they create a ProtoPie account by signing up.

![inviting-new-members](https://cdn.sanity.io/images/vidqzkll/production/aa66cfed1e963db56c019f809c5c07a44ef2c37a-1190x740.png/invite members.png)

### Changing Member Types

The team owner can assign team members as team admins by changing their member type from "member" to "admin." Once assigned as a team administrator, the team admin has the ability to delegate other team members as administrators.  

![changing-member-types](https://cdn.sanity.io/images/vidqzkll/production/8f9acd804af3584d082961e85c949da822713241-1493x839.png/member type.png)

### Assigning Roles

Both the team owner and team admins can assign roles to members. The two available roles are editor and viewer.

- **Viewers** have access to the projects and prototypes stored within their team space and leave comments on prototype pages to provide feedback.

- **Editors** can create prototypes in [ProtoPie Studio](https://www.protopie.io/learn/docs/introducing-protopie/protopie-ecosystem#proto-pie-studio), upload them to the cloud, utilize [team libraries](https://www.protopie.io/learn/docs/interaction-libraries/getting-started), create [interaction](https://www.protopie.io/learn/docs/interaction-recipes/getting-started) recordings, and utilize [ProtoPie Connect](https://www.protopie.io/learn/docs/connect/getting-started). 

 Learn more about [editors & viewers](https://www.protopie.io/learn/docs/teams/editors-and-viewers).

![assigning-roles](https://cdn.sanity.io/images/vidqzkll/production/b149f7976174694b0ee86e2b7f16cc5ecefc12d6-1518x772.png/roles.png)

### Removing Members

Team owners and admins can remove members from the team by following these simple steps:

1. Click on the three-dot menu next to the name of the member you want to remove.

1. Select âRemoveâ

If you need to bring back removed members, invite them using the same process as inviting new members.

![removing-members](https://cdn.sanity.io/images/vidqzkll/production/35e21a39b862cd7ffd4b60e8696ec5b2ee93871e-1563x938.png/remove.png)

## Managing Team Information & Billing

In the **General** section of the **Team settings** page, the team owner and team admins have the ability to change the name of the team and personalize the team logo. Additionally, the team owner can manage billing information and delete the team.

![managing-the-team](https://cdn.sanity.io/images/vidqzkll/production/f92f1b459bdbe0f431592771132b7ca0c8f0c769-2000x1440.png/general.png)

### Deleting Teams

As the team owner, you have the ability to delete a team. To be able to do so, you must ensure that all members have been removed from the team and that the Pro plan has been canceled.

If you are managing multiple teams in your account, make sure to give each one a unique name to easily identify them.

## Managing Projects

As a team member, you can manage all public and private projects. This includes changing a public project to a private project or archiving it. Learn moreÂ about [projects](https://www.protopie.io/learn/docs/teams/projects).

### Deleting Prototypes

Members of either public or private projects can delete any prototypes that have been created by either themselves or others within the project.

## Managing Fonts

*Available in the Enterprise plan only.*

### Uploading Custom Fonts to ProtoPie Cloud

To upload custom fonts to ProtoPie Cloud, both team admins and the team owner can follow these simple steps. We support font file formats such as TTF and OTF.

1. Navigate to Team settings within the team space.

1. Go to the Fonts section.

1. Click on the "Upload fonts" button, which will open the Upload fonts modal.

1. Add the font files by either dragging and dropping them into the modal or clicking on "upload files" to select the font files from your device. 

  1. The selected fonts will be listed for upload.

  1. The font name, weight, and style fields will be automatically populated based on the information from the font file.

  1. To add more fonts, click the "Add more fonts" option located in the bottom left corner of the modal.

  1. If needed, you can remove fonts from the upload list by using the delete icon located next to each uploaded font.

1. Click on the "Next" button.

1. Take the time to carefully review and agree to ProtoPie's Terms of Service and Privacy Policy.

1. Finally, click the "Agree & Upload" button to add the fonts to the fonts list.

**Important**: Before adding new fonts, it is crucial to verify that your organization possesses the legal rights to use and distribute the custom fonts being uploaded. ProtoPie cannot be held responsible for font licenses and their usage.

![team owner and the team admin can upload custom fonts](https://cdn.sanity.io/images/vidqzkll/production/cc3f90425e269050935c830c121b0ad5cc602aef-1440x659.png/team owner.png)

### Removing Custom Fonts from ProtoPie Cloud

The team owner and team admins can easily remove custom fonts from the fonts list by following these steps:

1. Navigate to Team settings and access the Fonts section.

1. Locate the custom font you want to delete and open the three-dot menu next to it.

1. Select the "Remove" option to remove the font from the list.


---

---
title: "Creating Test Rooms"
url: https://www.protopie.io/learn/docs/user-testing/creating-test-rooms
---

# Creating Test Rooms

# **Creating Test Rooms**

There are 4 ways to enter the test room creation flow:

1. **From Cloud Pie List (Single):** Click context menu (...) on a single Pie.

2. **From Cloud Pie List (Multiple):** Select multiple Pies and click "Create test room".

![Creating Test Rooms](https://cdn.sanity.io/images/vidqzkll/production/42c2b549e069343a3c7829ec5d178c2a64c60d9a-1280x720.gif/Cloud_Pie_List.gif)

3. **From Cloud Pie Viewer:** Click "Create test room" inside the viewer.

![Cloud Pie Viewer](https://cdn.sanity.io/images/vidqzkll/production/cdf3d1cc9fc86cdb769b4981970053e11c36e773-1280x720.gif/Cloud_Pie_Viewer.gif)

4. **From User Testing Menu:** Click "Create test room" in the main Cloud User Testing menu.

![Testing Menu](https://cdn.sanity.io/images/vidqzkll/production/532f85d2653524c506351366a914abd4e4403923-1280x720.gif/Testing_Menu.gif)

## Test Room Setup

### Adding Prototypes

Pie files can be added in two ways:

1. **Via URL**

1. **Selecting files from the cloud**

**Note:**

- *Limitation:* Local file upload is not supported; files must be on Cloud first.

- *Restriction:* Only **Public Projects** can be added. Private Projects are not allowed.

### Pie File Version Management

The test room stores a specific **revision**. To update, you must manually use the "**Update (Sync)**" feature.

**Important:**

- Pie files and revisions used in User Testing should not be deleted.

### Task Configuration

- **Task-Pie Assignment :** 

  - **1:1 Mapping:** Each task is linked to **one specific Pie file**.

  - **Flexibility:** You can assign the same Pie file to multiple tasks or use different Pie files for each task within a single test room.

- **Task Limit:** A test room can have up to **9 tasks**.

- **Capacity Limit:** The total capacity is limited to **1GB**.

### Setting Task Goals

Moderators record goals directly in the prototype preview:

- **Exact Path:** Record the specific interaction sequence.

- **Reach Final Scene:** Define the target final Scene.

- **Free Explore:** No recording needed.

![Setting Task Goals](https://cdn.sanity.io/images/vidqzkll/production/182a3e8bdcbba060010d5eb6b4f9e5f507564414-1216x1349.png/Screenshot 2026-01-27 at 6.53.15â¯PM.png)


---

---
title: "External Integrations"
url: https://www.protopie.io/learn/docs/user-testing/external-integrations
---

# External Integrations

# External Integrations

You can still integrate ProtoPie with external tools for unmoderated testing:

- **Supported Tools:** Useberry, Lookback, UserTesting, UserZoom.

- **Workflow:** Generally involves ensuring the prototype is Public and using the "Share > Copy Link" feature to paste into the external tool.

## User Testing with ProtoPie & Useberry

Easily set up unmoderated user testing with ProtoPie and Useberry in your desktop or mobile browser:

1. Open the prototype that you want to test in [ProtoPie Cloud](https://cloud.protopie.io/).

1. Make sure that anyone with the link can view your prototype. [Learn more](https://www.protopie.io/learn/docs/cloud/sharing-prototypes#allowing-anyone) about access settings.

1. Click on **Share** and select **copy link**.

1. Use this link to add a new prototype into your Useberry workspace.

[Learn more](https://protopie.io/blog/protopie-useberry) in detail how to use ProtoPie and Useberry together.

## User Testing with ProtoPie & Lookback

Easily set up unmoderated usability testing with ProtoPie and Lookback on desktop or mobile browsers, or with ProtoPie Player on iOS, iPadOS, and Android.

[Learn](https://www.protopie.io/blog/usability-testing-with-lookback) in detail how to use ProtoPie and Lookback together.

## User Testing with ProtoPie & UserTesting

Easily set up unmoderated usability testing with ProtoPie and UserTesting, using the desktop or mobile browser, or ProtoPie Player on iOS, iPadOS, and Android.

[Learn](https://www.protopie.io/blog/usability-testing-with-usertesting) in detail how to use ProtoPie and UserTesting together.

## User Testing with ProtoPie & UserZoom GO

You can easily set up unmoderated usability testing with ProtoPie & UserZoom GO in the desktop or mobile browser, or ProtoPie Player on iOS, iPadOS, and Android.

[Learn](https://www.protopie.io/blog/usability-testing-with-userzoom-go) in detail how to use ProtoPie and UserZoom GO together.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/user-testing/getting-started
---

# Getting Started

# User Testing

## Launch Notice

**From Beta to Product:** Previously offered as a Beta feature with limited functionality, User Testing is now launching as a comprehensive add-on product (Phase 2)

**ProtoPie User Testing** provides an environment where you can conduct usability tests directly on ProtoPie Cloud using prototypes with users.

User Testing goes beyond simple real-time observation by helping designers and researchers automatically gain **quantitative and actionable insights:**

- **Test success/failure rates**

- **User paths**

- **Key error data**

## Key Features

### 1. Goal-Based Task Types

When creating a test room, you can select from three types of tasks to set clear success criteria:

- **Exact Path:** Participants must follow a specific sequence of interactions defined by the moderator. Useful for verifying efficiency of specific flows.

- **Scene:** Participants are successful if they reach a predefined final scene, regardless of the path taken. Suitable for open-ended tests.

- **Free Explore:** No success criteria defined. Users freely explore the prototype to evaluate general usability.

![Key Features](https://cdn.sanity.io/images/vidqzkll/production/fe28b510fa1e9e1665f4cf3c6df624f34fa4d371-2714x1758.png/Screenshot 2026-01-27 at 6.59.07â¯PM.png)

### 2. Automated Results Reporting

View automatically generated analysis reports in the test room's **Results tab:**

- **Quantitative Metrics:** Task success rate and average task duration.

- **Path Analysis:** Detailed metrics including number of participants, average duration, and invalid actions for each path.

- **Top First Actions:** Shows the most common initial actions taken by users.

![Automated Results](https://cdn.sanity.io/images/vidqzkll/production/ad4d7fa84b11cd3d34264e5c335d802ff787ed83-3378x2048.png/Screenshot 2026-01-27 at 7.00.38â¯PM.png)

### 3. Interactive Session Replay & Highlights

Participants' test processes are recorded based on events for rich analysis:

- **Interaction Data Tracking:** Tracks clicks, scrolls, taps, swipes, and double taps with detailed timestamps.

- **Highlights:** Moderators can create independent playback units from specific segments of the full session.

![Interactive Session Replay](https://cdn.sanity.io/images/vidqzkll/production/1bfca1406b4b27c6a80436f70ddf395e9818c64a-2000x1173.png/Screenshot 2026-01-27 at 7.01.59â¯PM.png)


---

---
title: "Managing Test Sessions"
url: https://www.protopie.io/learn/docs/user-testing/managing-test-sessions
---

# Managing Test Sessions

# Managing Test Sessions

## Test Room Statuses

The room transitions through states which determine data collection and editability

**Draft**

- Preparation mode. No data collected.

- **Editable**: Tasks can be modified. 

**In Progress**

- Active or scheduled. Enters this state after first participant joins.

- **Partially Editable**: Cannot change Pie files to ensure consistency. Meta info is editable.

**Live**

- Participant is currently in session; recording in progress.

- **Not Editable**.

**Archived**

- Tests completed. Records preserved.

- **Not Editable**.

## Session Roles

- **Moderator:** An Editor who clicks `[Start testing]`. Manages the session and creates highlights.

- **Observer:** Team members (Editors or Viewers) who monitor the session in real-time.

- **Participant:** Invited users whose behavior is recorded. They can complete or abandon tasks using the `[End task]` button.

![Session Roles](https://cdn.sanity.io/images/vidqzkll/production/15938e8f69d56b6387f698f756f7d02ea89cdc84-2000x1307.png/Screenshot 2026-01-27 at 9.22.00â¯PM.png)

## Test Execution

### Session Preparation

- **Access:** Participants enter via URL/QR code and a passcode (refreshes every 3 minutes).

- **Device Requirements:** Desktop/mobile browser, or ProtoPie Player App (6.23.0+) on iOS/Android.

- **Participation Limit:** Only **one participant** per session.

- **Time Limit:** 20 minutes per task is recommended.

![Sharing Permission](https://cdn.sanity.io/images/vidqzkll/production/4244f8335c82a12c9607bedcb774ad3c16efb6ed-1790x1250.png/SharingPermissions.png)

### Real-time Observation

- **Monitoring:** Moderators and observers can watch the test process in real-time.

- **Mirroring:** Uses "Broadcast & watch" mechanism for screen mirroring.

![Moderated Testing](https://cdn.sanity.io/images/vidqzkll/production/b41956089b2a13f74bdbcddcdd181f8c4e54f14f-1280x720.gif/Moderated_Testing.gif)

### Test Completion & Recovery

- **Ending:** When a participant reaches the 'Thank You' page, the session ends, recording stops, and the room status clears "Live" status.

- **Disconnection:** If a participant disconnects, the system waits **5-10 minutes** for them to reconnect to the same session.

## Terminology

**Test Room: **A virtual space configured for user testing, serving as a container that includes one or more tasks and prototypes.

**Task: **An individual task that participants must perform within a test room, which can have success criteria set.

**Session: **The entire actual test process where moderators and participants sequentially perform multiple tasks together.

**Task Recording: **The recording captured for each individual task within a session. Screen interactions and timestamp data are collected separately for each task.

**Highlight: **A marker indicating noteworthy moments or important insights during User Testing result analysis, used to quickly find and share meaningful segments during session replay.


---

---
title: "Test Results & Analysis"
url: https://www.protopie.io/learn/docs/user-testing/test-results-and-analysis
---

# Test Results & Analysis

# Test Results & Analysis

The Result tab provides a comprehensive view of participant test results for each task. Once testing is complete, you can view automatically generated detailed analysis results in the **Results tab**. The displayed results vary depending on the task type (Exact Path, Reach Final Screen, Free Explore).

> **Note:** The Result tab is only accessible after the first participant's data has been collected.

## Statistics

Key statistical metrics are provided for each task type.

![Results Tab](https://cdn.sanity.io/images/vidqzkll/production/b4012acb796a24c93de1a953cb80fb73ed788545-1280x720.gif/Results_Tab.gif)

### Exact Path Tasks

For Exact Path tasks, the following metrics are displayed:

- **Avg. Path Match Score**: Average rate of how closely all participants followed the set target path.

- **Total Avg. Duration**: Average task completion time for participants.

- **Paths**: Number of participants, average duration, and average Invalid actions for each path.

- **Top first actions**: The most frequently selected first actions by participants.

### Scene Tasks

For Reach Final Screen tasks, the following metrics are displayed:

- **Success Rate**: Percentage of participants who reached the final screen.

- **Total Avg. Duration**: Average task completion time for participants.

- Success/failure results for each participant.

### Free Explore Tasks

For Free Explore tasks, the following metrics are displayed:

- Analysis of various paths chosen by participants.

- Number of participants and average duration per path.

## Individual Session Recordings

All interactions including clicks, scrolls, taps, and swipes are recorded in detail with timestamps.

Clicking on individual participants in the participant list allows you to:

- Replay that participant's entire test process.

- View all interactions with precise timestamps.

- Create highlights from important moments.

- Export the complete interaction list as a CSV file for further analysis.

## Highlights

You can save noteworthy moments as **highlights** while replaying individual participant session recordings:

- You can create highlight collections by selecting specific segments during recording playback.

- Highlights are useful for quickly finding and sharing important insights such as points where users struggled or unexpected behaviour patterns.

- Created highlight collections can be replayed in a separate window.

### Creating Highlights

You can save noteworthy moments during session replay to share insights:

1. **Select:** Click a participant to replay their session.

1. **Segment:** Select a specific timeframe in the recording.

1. **Save:** Name the highlight and add descriptions.

![Highlights](https://cdn.sanity.io/images/vidqzkll/production/fedcfdbcc4ac90de25ec8bd8bae8f8e6116e10a6-1280x720.gif/Highlights2.gif)


---

---
title: "User Testing on ProtoPie Cloud"
url: https://www.protopie.io/learn/docs/user-testing/user-testing-protopie-cloud
---

# User Testing on ProtoPie Cloud

# User Testing on ProtoPie Cloud

User testing is a critical component of the design process, helping to ensure that products and services meet the needs and expectations of users. By understanding how users navigate a product, what features they use, and what issues they encounter, designers and developers can make informed decisions to improve the user experience.

ProtoPie provides a secure test environment where you can test your prototypes and watch what the user is doing in real time. Create a test room within ProtoPie, observe how users interact with your prototype, and identify areas for improvement. 

## Creating a Test Room

You can create a test room in ProtoPie depending on whether you're testing a single or multiple prototypes.

### **For a Single Prototype**

1. Open the Pie (prototype) link.

1. Select **Create test room** in the top-right corner.

![Create a Test Room via Pie Link](https://cdn.sanity.io/images/vidqzkll/production/d2ba7a88439faaf59b25f467b1f0c51e925a4ce7-1914x1080.png/UT - Single Prototype.png)

### **For Multiple Prototypes**

**Option 1: From the Projects Tab**

1. Open your **Project** space.

1. Select the prototypes you want to test by clicking on the top left checkbox.

1. Click on the **Create test room** button in the upper right corner.

![creating test room](https://cdn.sanity.io/images/vidqzkll/production/f973839a24794d5e2c0a2c8c36e8962deb945083-1914x1080.png/UT - Projects Sidebar.png)

**Option 2: From the User Testing Tab**

1. Navigate to **User testing** from the left sidebar.

1. Click **Create test room** in the top-right corner.

1. Select multiple prototypes from your project folders to create a Test Room.

![Create a Test Room via User Testing Tab](https://cdn.sanity.io/images/vidqzkll/production/1cbed38843a0330cd6f12fe84d80f46a4b3a6a2d-1914x1080.png/UT - User Testing Sidebar.png)

A Test Room is created using the name of your first Pie file. You can rename the Test Room at any time. 

## Conducting User Testing

To start user testing, invite users to test your prototypes by having them scan the enlarged QR code or input the URL link. 

1. Ask users to open their cameras and scan the QR code or input the URL link on their browser. *The link & QR code cannot be opened via the Player app.*

1. Provide users with the **interim password** that appears to access the Test Room. 

1. Once users are in the Test Room, click on the **Start testing** button to observe user interaction in real time. You can stop or restart sharing the prototype at any time if necessary.

![conducting user testing](https://cdn.sanity.io/images/vidqzkll/production/7fda716a7e79cb5d0889c7143eb5152002e7367b-1914x1080.png/UT - Conduct UT.png)

## Moderator View

The moderator interface includes the **Start testing** and **Share** buttons in the header.

In the Pies list sidebar, moderators can view and select tasks to control what participants will do during the session. A new **Manage Pies** button has been added, allowing moderators to add or remove Pie files as needed.

Sharing options are available via the **Share** button, and the **Restart and Scene Change** dialog appears as a floating window in the center of the screen.

![conducting user testing](https://cdn.sanity.io/images/vidqzkll/production/f88a7b47fe7ca99afe9eb43dc0fd1365c2142b79-1914x1080.png/UT - Moderator View.png)

## Share Your Test Room

After setting up a test room, you can share it with participants and observers. Use the Share button to open a dialog where youâll find unique links for each group.

![conducting user testing](https://cdn.sanity.io/images/vidqzkll/production/bf98562b8a33ed4199de9e3ca791dc0e189a85fb-1914x1080.png/UT - Share Option.png)

### Invite Participants

The **participant link** is for people who will actively join the session. When they open the link, they can enter the test room and interact with the test environment. Each session generates a secure, unique link so only invited participants can join.

### **Invite Observers**

The **observer link** lets teammates and stakeholders watch the session in real time without participating. Observers can follow the session live but will not be able to interact.

You control who can use the observer link:

- Allow all organization members to join for broad visibility.

- Limit access to members of specific team spaces for more focused sharing.

This gives you flexibility to include the right people while keeping control over access.

## Managing Prototypes

Only editors can be moderators. Viewers can join the test rooms as observers (view participantsâ interactions) but cannot edit the Test room.

To add or update prototypes, select **Manage Pies** in the Pies list on the left. A window with your active projects will open, where you can add or remove Pies for testing. You can include up to **9 Pies** in total, or up to **1 GB of storage**. 

![updating prototypes to be tested](https://cdn.sanity.io/images/vidqzkll/production/0571c47dda7dcb811ecef0e2606fcbd3ec0e66a0-1914x1080.png/UT - Manage Pies.png)

These features are currently in closed beta, available to select ProtoPie Enterprise customers. [Contact Sales](https://www.protopie.io/form/request-demo) if your organization is interested.


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/variables/getting-started
---

# Getting Started

# Variables

Variables can be described as "baskets" that hold valuable information. You can store various data like names, passwords, or account balances in these baskets for later use. You can flexibly create dynamic interactions by modifying the values within variables and detect how their values change.

[Video: ](https://www.youtube.com/watch?v=TQYzTD9rB0E)

Completely new to variables? Check out the examples on this page to get the most out of this powerful feature.

- [Predefined variables](https://www.protopie.io/learn/docs/variables/predefined-variables) â A set of variables that are always accessible in your prototypes. The values they store update automatically. 

- [Use cases](https://www.protopie.io/learn/docs/variables/use-cases) âÂ A selection of practical use cases involving variables. 

## Difference Between Variables & Formulas

Formulas and variables work together seamlessly to enhance your prototypes. Here's a quick breakdown of their relationship:

- **Variables**: Think of variables as handy "baskets" that hold values. They allow you to store and retrieve data, making it easier to reuse information throughout your prototype. Variables can be used independently or in conjunction with formulas. For example, you use formulas to retrieve a value stored in a variable.

- **Formulas**: Formulas are expressions that calculate and "return" a result. They are powerful tools for creating dynamic interactions. You can use formulas to perform calculations, manipulate text, and accomplish various tasks. Formulas can also include variables to access stored values.

The synergy between formulas and variables allows you to take your prototypes to the next level. Variables store values that can be utilized by formulas, while formulas can even be stored within variables to be reused across scenes.

In summary, formulas and variables complement each other, offering flexibility and efficiency in your prototype development process.

[Learn more](https://www.protopie.io/learn/docs/formulas/getting-started) about formulas.

## Choosing the Variable Scope

There are two types of variable you can choose from.

### For All Scenes

A **variable for all scenes** can be accessed in every scene within your prototype. It's perfect for transferring data between scenes. For example, if you modify the value of a variable for all scenes in Scene A, the changes affect every instance where the variable is used across the prototype.

### For This Scene

A **variable for this scene** is specific to the scene where you created it. It cannot be used in Scene B if it was created in Scene A. Also, this type of variable can hold formulas too.

## Using Data Types

A variable can store three types of data: **text**, **number**, or **color**.

### Text

Text variables are used to store text values. If you use a number as a value, the text variable will use it as a text.

### Number

Number variables store numbers. They canât hold data that arenât numbers.

### Color

Color variables store hex color code values. They canât hold data that arenât hex color codes.

## Using Assign & Detect

Variables are typically manipulated with the **Detect** trigger and **Assign** response.

### Assign Response

Itâs used to assign new values to variables. It can be a text, number, or color data type. Additionally, such values can be inputted directly or dynamically generated through a formula.

[Learn more](https://www.protopie.io/learn/docs/interactions/responses#assign) about Assign.

### Detect Trigger

Itâs used to keep track of changes in a variable. It allows you to trigger responses based on whatever changes take place in a specific variable.

[Learn more](https://www.protopie.io/learn/docs/interactions/triggers#detect) about Detect.

## Displaying Variables

The values inside variables can be displayed on the canvas and in the preview window of ProtoPie Studio by using **dedicated debuggers**. You can enable them by clicking on the bug icon next to the variable name in the variable panel. This way, you can always check if the value stored by the variable is updating correctly.

![displaying-variables](https://cdn.sanity.io/images/vidqzkll/production/0ef28200d67addccc1ffc8b20176339967b9ef10-1580x864.png/displaying-variables.png)

## Learning the Basics

Creating interactions with variables in ProtoPie is simpler than you think. This video shows you how you can quickly create a dynamic animation using variables.

[Video: ](https://www.youtube.com/watch?v=YXB9qoknY4s)

## Practicing with Examples

### Making a Spinner

You can animate a simple spinner using variables. This example shows you how to increase or decrease the value of a variable by 1. The text layer will then display the value of the variableâevery time it changes. 

![making a spinner](https://cdn.sanity.io/images/vidqzkll/production/a63e9c386ba78a75ee2a0bc208d467bf784de39d-1076x228.gif/formula_spinner.gif)

[Video: ](https://www.youtube.com/watch?v=P57LwLzbbJI)

### Making a Ripple Effect

Animate a quick ripple effect with predefined variables. This example shows you how to create a ripple effect based on where a touch event takes place.

[Learn more](https://www.protopie.io/learn/docs/variables/predefined-variables) about predefined variables. 

![ripple effect](https://cdn.sanity.io/images/vidqzkll/production/46b1d28959d926922b4bcb8d01550488d3e7b44c-1076x228.gif/formula_ripple.gif)

[Video: ](https://www.youtube.com/watch?v=1KaQDu3IwuM)

Looking for practical use cases? [Learn more](https://www.protopie.io/learn/docs/variables/use-cases) with some practical use cases involving variables.

Ready to take your skills to the next level? Join the [**ProtoPie Masterclass**](https://learn.protopie.io/course/masterclass-in-advanced-prototyping-for-digital-dashboard)** **and** **unlock the power of variables in your prototypes. Learn how to create dynamic interactions using text, numbers, colors, and predefined variables.

By joining the ProtoPie Masterclass, you'll rapidly enhance your skills and effortlessly create advanced prototypes. Don't miss out on this opportunity to level up!


---

---
title: "Predefined Variables"
url: https://www.protopie.io/learn/docs/variables/predefined-variables
---

# Predefined Variables

# Predefined Variables

Predefined variables are a set of variables that are always accessible in your prototypes. The values they store update automatically.

For example, the value of $mouseX will always change automatically, depending on wherever the cursor finds itself. 

[Learn more](https://www.protopie.io/learn/docs/variables/getting-started) about using variables.


---

---
title: "Variables Use Cases"
url: https://www.protopie.io/learn/docs/variables/use-cases
---

# Variables Use Cases

# Variables Use Cases

Explore the practical application of variables for various use cases. Learn how to effectively use different variable scopes and data types, predefined variables, and how these work in various [triggers](https://release-docs.protopie.io/learn/docs/interactions/triggers) and [responses](https://release-docs.protopie.io/learn/docs/interactions/responses). Experience the prototypes firsthand by trying them out and downloading them to observe the interactions.

Learn more about [variables](https://www.protopie.io/learn/docs/variables/getting-started) and [formulas](https://www.protopie.io/learn/docs/formulas/getting-started).

Find the use case you need below:

- [Bunny vs. Wolf game](https://learn/docs/ko/variables/use-cases#bunny-wolf-game)

- [Range slider](https://www.protopie.io/learn/docs/variables/use-cases#range-slider)

- [Using data elsewhere](https://www.protopie.io/learn/docs/variables/use-cases#using-data-elsewhere)

- [Calculating the remaining balance](https://www.protopie.io/learn/docs/variables/use-cases#calculating-the-remaining-balance)

- [Remembering what's in the shopping cart](https://www.protopie.io/learn/docs/variables/use-cases#remembering-what-s-in-the-shopping-cart)

- [Timer](https://www.protopie.io/learn/docs/variables/use-cases#timer)

- [On-scroll sticky header](https://www.protopie.io/learn/docs/variables/use-cases#on-scroll-sticky-header)

- [Enabling a keyboard view](https://www.protopie.io/learn/docs/variables/use-cases#enabling-a-keyboard-view)

- [Using the incoming speech](https://www.protopie.io/learn/docs/variables/use-cases#using-the-incoming-speech)

Looking for formula-specific use cases? Check out the [use cases involving formulas](https://www.protopie.io/learn/docs/formulas/use-cases).

Find tips, tricks, and solutions about variables and formulas that other users have shared before in our communities.

- [ProtoPioneers Community](https://community.protopie.io/home)

- [ProtoPie YouTube channel](https://www.youtube.com/c/ProtoPie/featured)

- [ProtoPie Users on Facebook](https://www.facebook.com/groups/ProtoPieUsers/)

## Bunny vs. Wolf Game

Create variables to keep track of the score in a Bunny vs. Wolf game prototype.

![bunny-wolf-game](https://cdn.sanity.io/images/vidqzkll/production/4b17843e42515c729e965fa40aa3e549c6fc5972-1348x1010.gif/variable-game-use-case.gif)

[Try the prototype ](https://cloud.protopie.io/p/06e9c95d36d9e4cf3d5bc180)yourself.

Learn more in the [**Mobile Game prototyping masterclass**](https://learn.protopie.io/course/mobile-game-prototyping-masterclass).

## Range Slider

Link the position of the handle with a range of values. As you drag and move the handle, the latest value is stored in a variable.

![range slider](https://cdn.sanity.io/images/vidqzkll/production/bcd7cf148b9edeba5acb35a4f40a100128818cae-1718x1298.gif/range slider.gif)

[Try the prototype](https://cloud.protopie.io/p/d60c5e3a05) yourself.

Learn more about the [Chain trigger](https://www.protopie.io/learn/docs/interactions/triggers#chain), [Detect trigger](https://www.protopie.io/learn/docs/interactions/triggers#chain), and [functions](https://www.protopie.io/learn/docs/formulas/functions).

## Using Data Elsewhere

Store the input from the input layer in a variable, and use it elsewhere, e.g., in a different scene. Think of names, passwords, email addresses, etc., that a user would enter and you want to use throughout the prototype.

![using data elsewhere](https://cdn.sanity.io/images/vidqzkll/production/6b8bb38465b6bb612ec398355034bdda0aa801c7-1842x1318.gif/using data elsewhere.gif)

[Try the prototype](https://cloud.protopie.io/p/1b6fadf332) yourself.

Learn more about the [Detect trigger](https://www.protopie.io/learn/docs/interactions/triggers#detect), [Start trigger](https://www.protopie.io/learn/docs/interactions/triggers#start), and [layer properties](https://www.protopie.io/learn/docs/formulas/layer-properties).

## Calculating the Remaining Balance

Calculate the remaining balance when doing a bank transfer. To do the actual calculation, use arithmetic operations subtracting the transfer amount from the current balance. 

![calculating the remaining balance](https://cdn.sanity.io/images/vidqzkll/production/6ef94b3af89a76dbbdf4ac29ae71f4b13a825a62-1714x1306.gif/calculatind the remaining balance.gif)

[Try the prototype](https://cloud.protopie.io/p/bb3c9801ef) yourself.

Learn more [arithmetic operations](https://www.protopie.io/learn/docs/formulas/syntax#arithmetic-operations), [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition), and [components](https://www.protopie.io/learn/docs/components/getting-started).

## Remembering What's in the Shopping Cart

Add items to the shopping cart, and calculate and display the total amount in the shopping cart dynamicallyâdepending on what items were added.

![shopping cart](https://cdn.sanity.io/images/vidqzkll/production/54f389e4afd2890822881ce59af4d2eaf32851c4-1688x1250.gif/shopping cart.gif)

[Try the prototype](https://cloud.protopie.io/p/ea75d31bc7) (made by [Soda Design](https://www.protopie.io/blog/protopie-101-for-beginners-by-soda-design)) yourself.

Learn more about [arithmetic operations](https://www.protopie.io/learn/docs/formulas/syntax#arithmetic-operations), [functions](https://www.protopie.io/learn/docs/formulas/functions), and [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition).

## Timer

After every 60 seconds, the timer adds another minuteâjust like any basic timer does. However, you can create any timer you like. The opposite, a countdown timer, is possible too. 

![timer](https://cdn.sanity.io/images/vidqzkll/production/e4c20817ffda518dd53b7d45c706882174c4e4a2-1215x790.gif/timer 2.gif)

[Try the prototype](https://cloud.protopie.io/p/67fb5179b9) yourself.

Learn more about the [arithmetic operation](https://www.protopie.io/learn/docs/formulas/syntax#arithmetic-operations)[s](https://formulas-syntax-doingcalculations-arithmeticoperationspart/), [conditions](https://www.protopie.io/learn/docs/interactions/responses#condition), and the [Detect trigger](https://www.protopie.io/learn/docs/interactions/triggers#detect).

## On-Scroll Sticky Header

Distinguish an upward and downward scroll and adjust the position of the sticky header accordinglyâall using a single predefined variable: $touchVelocityY.

![scroll sticky header](https://cdn.sanity.io/images/vidqzkll/production/228c16e4a390cf0c8f5c4071b7c6f561862dc2b8-1810x1312.gif/scroll sticky header.gif)

[Try the prototype](https://cloud.protopie.io/p/f6558c8c61) yourself.

Learn more about [predefined variables](https://www.protopie.io/learn/docs/variables/predefined-variables) and the [Detect trigger](https://www.protopie.io/learn/docs/interactions/triggers#detect).

## Enabling a Keyboard View

When the keyboard appears from the bottom, move your designs based on the keyboard height. Do these calculations automatically using the predefined variable $keyboardHeight.

![enabling keyboard view](https://cdn.sanity.io/images/vidqzkll/production/9bd3d9a2d30cecc71a1f4a455365e52ad2dab0be-1654x1308.gif/enabling a keyboard view.gif)

[Try the prototype](https://cloud.protopie.io/p/cae874c8a3) yourself.

Learn more about [predefined variables](https://www.protopie.io/learn/docs/variables/predefined-variables) and the [Focus trigger](https://www.protopie.io/learn/docs/interactions/triggers#focus).

## Using the Incoming Speech

Use the incoming speech whenever listening to voice commands is enabled, using the predefined variable $voiceTranscript. Display the transcript via a Text response or make the prototype read it out loud. 

[Video: ](https://www.youtube.com/watch?v=WdTq7o-v2N4)

[Try the prototype](https://cloud.protopie.io/p/48bb54f310) yourself.

Learn more about [predefined variables](https://www.protopie.io/learn/docs/variables/predefined-variables) and [voice prototyping](https://www.protopie.io/learn/docs/voice-prototyping/getting-started).


---

---
title: "Getting Started"
url: https://www.protopie.io/learn/docs/voice-prototyping/getting-started
---

# Getting Started

# Voice Prototyping

With ProtoPie's voice prototyping features, you can add realistic voice interactions to your prototypes using speech-to-text (STT) and text-to-speech (TTS) capabilities. Imagine voice commands that are recognized and text that is spoken out loudâcreating a truly immersive experience.

By incorporating conversation design and voice interactions, you can easily create prototypes for accessibility, voice search, voice assistants, dictation apps, and so much more. It goes beyond traditional touch interactions, opening up new possibilities.

Creating voice interactions involves 1 trigger and 2 responses. The [Listen response](https://www.protopie.io/learn/docs/interactions/responses#listen) enables your prototype to listen for voice commands. To trigger responses based on voice commands, you can use the [Voice Command trigger](https://www.protopie.io/learn/docs/interactions/triggers#voice-command). Remember, the Listen response is always required before using the Voice Command trigger. 

[Video: Check out this Quick Start lesson.](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DSx0eJ1IZa8A&feature=youtu.be)

In addition, the Speak response allows your prototype to "speak" by reading text aloud.

As long as your computer or smart device has a microphone and internet access, you can enjoy prototypes with voice interactions. It works seamlessly in the following environments:

Speech-to-text interactions

- Preview window of ProtoPie Studio

- ProtoPie Player

- ProtoPie Cloud

  - Google Chrome on desktop

  - Google Chrome on Android

Text-to-speech interactions

- Preview window of ProtoPie Studio

- ProtoPie Player

Supported languages for voice prototyping

- 52 languages and language variants for listening.

- 40 languages and language variants for speaking.

Send Feedback

Voice prototyping is currently in Beta. Your input is essential in making it even better! Whether you have suggestions for improvements or any other feedback, we would love to hear from you.

## Learn by Doing

### Voice Prototyping Masterclass

Learn to use above interactions effectively by engaging in interactive conversation exercises and studying real-world speech examples with the [Masterclass in Advanced Voice Prototyping](https://learn.protopie.io/course/masterclass-in-advanced-voice-prototyping), a transformative project led by industry experts. 

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dl0CKUkUCK20)

 

### TV and Video Streaming UI Masterclass

A newly released masterclass. Learn how to prototype  rich interactive TV interfaces   using real-world examples i.e streaming channels such as Netflix, Disney Plus, etc.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D2qYNGzwiedI)

 

### Use Cases

Explore  practical [uses cases](https://www.protopie.io/learn/docs/voice-prototyping/use-cases) to  learn more about what is possible to achieve using the voice prototyping feature.


---

---
title: "Listen Response"
url: https://www.protopie.io/learn/docs/voice-prototyping/listen-response
---

# Listen Response

# Listen Response

In order for your prototype to respond to voice commands, you'll need to enable the listening feature. By default, voice commands are not picked up. To make your prototype listen,  use the **Listen** response.

![listen-response](https://cdn.sanity.io/images/vidqzkll/production/b342f5f4e5e20cac327e74554178c5a51c22ecaf-2175x1020.png/Listen Response.png)

In this example, tapping the oval shape activates listening to voice commands.

## Continuous Listening

When you enable listening to voice commands in your prototype, the listening feature will automatically stop when no speech is detected. However, if you want to ensure that listening remains enabled even during moments of silence, you can check the **Continuous **option.

By checking the Continuous mode, your prototype will continue listening even when no voice commands are being picked up. This allows for a seamless user experience and eliminates interruptions caused by brief pauses. Prototypes can listen to voice commands continuously for up to 5 minutes. 

When Continuous mode is checked, you will need a separate Listen response to explicitly stop listening.

## Language Options

Use the **Spoken Language** menu to choose one of the 52 languages and language variants available.

## Recording Voice Interactions in Preview

Record your prototype's media sounds and voice interactions by using an external microphone. Click the Settings icon in the Preview window and choose the desired audio input device.

![audio recording in preview window](https://cdn.sanity.io/images/vidqzkll/production/515428b5cedce83f40327b817a53d1e8760fd66d-2000x1103.png/audio-recording_(1).png)

 

## Voice Prototyping Masterclass

Join the [Masterclass in Advanced Voice Prototyping ](https://learn.protopie.io/course/masterclass-in-advanced-voice-prototyping)and learn from industry professionals with extensive experience in voice prototyping. 

Learn how to utilize a **cancellable timer** for improved time management and enhanced user experience; break down complex problems into manageable steps using a** recursive looping mechanism, **and more**.**


---

---
title: "Speak Response"
url: https://www.protopie.io/learn/docs/voice-prototyping/speak-response
---

# Speak Response

# Speak Response

The Speak response allows your prototype to "speak" by reading text aloud, as-is, or via a formula. 

## Text

Enter the text that needs to be read out loud here.

![speak response](https://cdn.sanity.io/images/vidqzkll/production/7e2053f1f483c28536d29e13e60daf400dce9555-2175x1305.png/speak response.png)

In this example, tapping the logo triggers this speech: "ProtoPie is the most intuitive way to prototype and perfect them".

## Formula

You can use formulas to create dynamic voice interactions, as long as the formula returns a text. Additionally, you can use the predefined variable $voiceTranscript, which stores the latest voice command.

### Voice Options

You can customize the voice style by choosing a language, type of voice, speed, and pitch.

### Language

You can choose from 40 languages and language variants.

### Voiced by

You can choose between a female or male voice per language.

### Speed

You can adjust the speed by choosing a value between 0.5 and 2.

### Pitch

You can adjust the pitch angle by choosing a value between 0.5 and 2.

![pitch](https://cdn.sanity.io/images/vidqzkll/production/e9b0a1a301fbfc95cf06d63f30dd38cab8e7036d-2175x630.png/pitch.png)

In this example, once listening is enabled, the prototype will start reading out loud whatever speech the incoming voice command contains.

## Recording Voice Interactions in Preview

Record your prototype's media sounds and voice interactions by using an external microphone. Click the Settings icon in the Preview window and choose the desired audio input device.

![record audio in preview mode](https://cdn.sanity.io/images/vidqzkll/production/515428b5cedce83f40327b817a53d1e8760fd66d-2000x1103.png/audio-recording_(1).png)

 

## Voice Prototyping Masterclass

Gain expertise in designing and developing voice interfaces that enhance user experiences and Acquire practical skills through hands-on exercises and real-world projects with the [Masterclass in Advanced Voice Prototyping](https://learn.protopie.io/course/masterclass-in-advanced-voice-prototyping). 

Don't miss this opportunity to become a master of advanced voice prototyping.


---

---
title: "Use Cases"
url: https://www.protopie.io/learn/docs/voice-prototyping/use-cases
---

# Use Cases

# Use Cases

Explore real-world applications of the voice prototyping feature. Experience it firsthand by opening the shared Pie files for each use case to see which triggers and responses were used to achieve these interactions. 

Find the use case you need below:

- [Smart TV  voice search](https://www.protopie.io/learn/docs/voice-prototyping/use-cases#smart-tv-voice-search)

- [Smartphone voice assistant](https://www.protopie.io/learn/docs/voice-prototyping/use-cases#smart-tv-voice-search)

- [In-car voice control prototype](https://www.protopie.io/learn/docs/voice-prototyping/use-cases#in-car-voice-control-prototype)

- [Real time voice translation app](https://www.protopie.io/learn/docs/voice-prototyping/use-cases#real-time-voice-translation-app)

- [Google doc voice typing](https://www.protopie.io/learn/docs/voice-prototyping/use-cases#google-doc-voice-typing)

Check out  related lessons  in ProtoPie School and  go to the next level with our masterclasses. Join and embark on an enlightening journey through  comprehensive lessons that delve into the realms of wake word detection, voice commands, text processing, weather information, conversation handling,  playing songs and more 

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3Dl0CKUkUCK20)

- [

Voice assistant prototyping masterclass](https://learn.protopie.io/course/masterclass-in-advanced-voice-prototyping)

- [Mobile game prototyping masterclass](https://learn.protopie.io/course/mobile-game-prototyping-masterclass)

- [TV and video streaming UI  masterclass](https://learn.protopie.io/course/prototyping-for-tv-and-video-streaming-apps)

## Smart TV Voice Search

Use voice  commands to search for movies on a TV prototype used in a real device. Use ProtoPie Connect to fully interact with the prototype.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D1SJlMFqCqa8)

[Try the prototype ](https://cloud.protopie.io/p/60ee64cda0)yourself.

## Smartphone Voice Assistant

Create a voice assistant that recognizes speech, and interacts with you as you give it  voice commands. 

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DUvOzqtRVbyU)

[Try the prototype](https://cloud.protopie.io/p/2323a66a75) yourself.

## In-car Voice Control Prototype

Turn on the music in the car while driving  by using voice commands and speech recognition.

[Video: ](https://www.youtube.com/supported_browsers?next_url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D1iMocwsnw1E)

[Try the prototype](https://cloud.protopie.io/p/6ec7e70d1a?utm_source=youtube&utm_medium=organic-social&utm_campaign=demo-solution-automotive&utm_content=1iMocwsnw1E) yourself.

Follow this [tutorial](https://www.protopie.io/blog/how-to-create-an-in-car-voice-control-prototype).

## Real-time Voice Translation App

Use the  microphone on the Google translate app to  catch  your voice and   translate it to the language of your preference in real time.

[Video: ](https://www.youtube.com/watch?v=cO2aVfXr_9s)

[Try the prototype](https://cloud.protopie.io/p/b91edba11d?utm_source=youtube&utm_medium=organic-social&utm_campaign=demo-feature&utm_content=cO2aVfXr_9s) yourself.

## Google Doc Voice Typing

Let the Google Docs listen to the information you provide and write the content as you speak.  

[Video: ](https://www.youtube.com/watch?v=nA0gXpYAF4k)

[Try the prototype](https://cloud.protopie.io/p/b576a0cf7c?utm_source=youtube&utm_medium=organic-social&utm_campaign=demo-feature&utm_content=nA0gXpYAF4k) yourself.


---

---
title: "Voice Command Trigger"
url: https://www.protopie.io/learn/docs/voice-prototyping/voice-command-trigger
---

# Voice Command Trigger

# Voice Command Trigger

To trigger responses based on voice commands, simply use the Voice Command trigger. You have the flexibility to configure the trigger to work while someone is speaking or after they have finished speaking. Additionally, you can specify the phrases that should be recognized as commands, allowing you to include or exclude specific phrases.

To enable the Voice Command trigger, make sure to enable listening with the [Listen response](https://release-docs.protopie.io/learn/docs/voice-prototyping/listen-response). This will activate the voice recognition capabilities of your prototype.

To ensure the best performance and accuracy of voice interactions, here are some helpful tips:

1. **Stay close to the microphone**: Position yourself near the microphone to capture your voice clearly and accurately.

1. **Minimize background noise**: Find a quiet environment or reduce background noise to improve the recognition of your voice commands.

1. **Be articulate**: Speak clearly and enunciate your words to enhance the accuracy of voice recognition.

![voice command](https://cdn.sanity.io/images/vidqzkll/production/d65ffeac28fcc48e106a22ddee56673544cbb1be-2175x735.png/voice command.png)

In this example, tapping the oval shape activates listening to voice commands. The oval will change its color as soon as someone is speaking.

## Trigger Point

It determines at which point the responses should activate.

After Speaking

The responses activate when the prototype no longer detects a speech, meaning when someone stops speaking. This trigger point does not work when Continuous is active in the Listen response.

While Speaking

As soon as the prototype detects a speech, meaning when someone starts speaking.

## Command

When the "Command" option is active, a response will be triggered only if specific commands (words or phrases) are included or excluded from the speech.

Phrases - Include

This means that a voice command needs to include one of the phrases listed. You can enter various words, phrases, or sentences and separate them using line breaks.

![phrases-include](https://cdn.sanity.io/images/vidqzkll/production/d37b407eb58189c6ab12beff9617bbed60dd57e7-2175x1347.png/phrases-include.png)

In this example, the shape's opacity changes only if the incoming voice command includes at least one of the two phrases: "ProtoPie" and "Prototyping Tool".

Phrases - Exclude

This means that the voice command should not contain any of the phrases listed. You can enter various words, phrases, or sentences and separate them using line breaks.

![phrases-exclude](https://cdn.sanity.io/images/vidqzkll/production/25c78bfc420f8e4cdaac5af5447a1f1c3705757c-2175x1347.png/phrases-exclude.png)

In this example, the text response triggers only if the incoming voice command does not contain the phrase "ProtoPie".

No Phrases Detected

This means that the incoming speech does not contain any phrases. It could be due, for example, to background noises or other sounds that can't be interpreted as human language.

![no-phrases-detected](https://cdn.sanity.io/images/vidqzkll/production/5e4da226cfa10c04f2f33a74ea6039936350618d-2175x1347.png/no-phrases-detected.png)

In this example, "Please say it again" will be displayed via a Text response if no phrases are detected.

## Recording Voice Interactions in Preview

Record your prototype's media sounds and voice interactions by using an external microphone. Click the Settings icon in the Preview window and choose the desired audio input device.

![Recording Voice Interactions in Preview](https://cdn.sanity.io/images/vidqzkll/production/515428b5cedce83f40327b817a53d1e8760fd66d-2000x1103.png/audio-recording_(1).png)

## Voice Prototyping Masterclass

Master the effective application of these commands by actively participating in engaging conversation exercises and thoroughly analyzing real-world speech examples. 

The [Masterclass in Advanced Voice Prototyping](https://learn.protopie.io/course/masterclass-in-advanced-voice-prototyping) is a comprehensive program that equips you with the knowledge and tools needed to design and build cutting-edge voice-driven user interfaces.