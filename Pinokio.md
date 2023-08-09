
- [index](#index)
- [old](#old)
- [sharing](#sharing)
- [dna](#dna)
- [growth](#growth)
- [history](#history)
- [neuron](#neuron)
- [overview](#overview)
- [reproduction](#reproduction)
- [statemachine](#statemachine)
- [browser](#browser)
- [datastructure](#datastructure)
- [flow](#flow)
- [fs](#fs)
- [input](#input)
- [log](#log)
- [networking](#networking)
- [notify](#notify)
- [overview](#overview)
- [shell](#shell)
- [api](#api)
- [configure](#configure)
- [create](#create)
- [form](#form)
- [overview](#overview)
- [publish](#publish)
- [rpc](#rpc)
- [shell](#shell)
- [test](#test)
- [quickstart](#quickstart)
- [reference](#reference)
- [shell](#shell)
- [what](#what)
- [applemac](#applemac)
- [index](#index)
- [intelmac](#intelmac)
- [linux](#linux)
- [windows](#windows)
- [overview](#overview)
- [structure](#structure)
- [uri](#uri)
- [global](#global)
- [input](#input)
- [local](#local)
- [overview](#overview)
- [self](#self)
- [decode](#decode)
- [execute](#execute)
- [fetch](#fetch)
- [overview](#overview)
- [api](#api)
- [persistent](#persistent)
- [run](#run)
- [wait](#wait)
- [api](#api)
- [autostart](#autostart)
- [database](#database)
- [dependencies](#dependencies)
- [document](#document)
- [dynamic](#dynamic)
- [enter](#enter)
- [env](#env)
- [forms](#forms)
- [hello](#hello)
- [index](#index)
- [menu](#menu)
- [multiple](#multiple)
- [programming](#programming)
- [publish](#publish)
- [python](#python)
- [run](#run)
- [script](#script)
- [share](#share)
- [write](#write)

# index

<blockquote class='info'>

<h4>notice</h4>

<br>

Just like a web browser, Pinokio doesn't do anything on its own, but will become more and more useful as people build and share apps, workflows, and APIs around it.

<br>

To stay on top of all the new APIs and app integrations,

- Follow <a href="https://twitter.com/cocktailpeanut">@cocktailpeanut</a> on Twitter
- Join the <a href="https://discord.gg/TQdNwadtE4">Pinokio discord</a>
</blockquote>

# Pinokio

> AI Browser

Pinokio is a browser that lets you **install, run, and automate any AI applications and models** automatically and effortlessly.

No more opening the terminal. No more `git clone`. No more `conda install`. No more `pip install`. No more messing with execution environments.

**All of them automated with one click**, as easy as using a browser.


![pinokio.png](pinokio5.png)

## Run anything, in a browser.

There are so many applications that require you to open your terminal and enter commands, not to mention deal with all kinds of complicated environment and installation settings.

With Pinokio, all of this can be packaged into a simple JSON script, which can then be run in a browser setting with **just one click.**

### Terminal apps in the browser

Any CLI (command line interface) apps can be ported to run in the Pinokio browser. Some examples:

- **installation scripts:** `pip install`, `npm install`, etc.
- **python scripts:** any python script can be run with one click. No terminal required.
- **any shell command:** `mkdir`, `curl`, `git`, etc.
- **anything:** anything that can run in a terminal can be automated with Pinokio, in the browser.

### Servers in the browser

Running a server on a computer is not a trivial task. You need to open a terminal, and run a bunch of commands to start the server, and keep the terminal open to keep them running.

**Not anymore.**

Pinokio lets you can **launch servers and daemons directly in the app, with one click.**

Now anyone can run powerful server based apps on their own computer, effotlessly:

1. **Database Systems:** Elasticsearch, MongoDB, RocksDB, Vector Databases, etc.
2. **Decentralized Applications:** Bitcoin, IPFS, etc.
3. **AI Servers:** StableDiffusion Web UI, Gradio, Langchain apps, etc.
4. **Web apps:** Any web apps, really, can be run in the Pinokio browser.
5. **Bots:** Spin up bots that run in the background, in the Pinokio browser, with one click.


### Example

Anything a human can do on a computer, can be done automatically thanks to Pinokio. Here's an example:

![helloserver.gif](helloserver.gif)

In this example, Pinokio automatically:

1. creates a node.js project
2. installs libraries
3. writes a server for a web server
4. starts the server
5. opens a browser

All with ZERO human intervention, 100% automated.

## Automate Everything

### There's a script for that

Pinokio is an application that can autonomously read, write, process, and execute anything on your computer, with a simple scripting language. Pinokio can:

- compose files
- download files
- accumulate data
- install libraries and other applications
- run shell commands
- make network requests
- publish files
- browse the internet
- and **pretty much anything a human can do on a computer, without requiring humans.**


### Install and control any AI

With the ultimate automation capabilities, Pinokio can even automatically install and run various AI engines and models on the fly, and then script them to make decisions and execute tasks. Any AI 

- Open source AI
  - Language models: llama.cpp
  - Image models: Stablediffusion
  - Diffusers
  - Transformers
  - etc.
- AI frameworks and APIs
  - OpenAI API
  - Langchain
  - etc.

### Totally autonomous agents

Pinokio is already useful for running "one-click scripts" that autmoate all kinds of things. But we can go further.

Pinokio supports [totally autonomous agents that can run with ZERO human intervention](/tutorial/autostart).


## Feature Highlights

### Browse and Install

Browse and install anything, including AI engines (llama, stablediffusion, etc.) **with one click**.

![install.gif](install.gif)

### Run

Automate anything through script.

![run.gif](run.gif)

### Automate

Mix and match multiple scripts to execute complex tasks.

![automate.gif](automate.gif)

### Share

Instantly share the workflows, scripts, datasets, and everything over git.

[Everything in Pinokio is a file](fs/overview.html), therefore ultra-shareable.

![share.gif](share.gif)


## How it works

### How is it possible?

<br>

#### Built-in binaries

Pinokio ships with man of the common binaries you need when installing many AI applications, including:

1. Node.js/NPM
2. Python/Pip
3. Git
4. etc. (more to come)

It takees care of all the convoluted steps one must jump through (installing the prerequisites) so the users can simply try new apps and engines with one click.

<br>

#### Turing complete script

Pinokio has a native scripting language written in JSON, extending [JSON-RPC](https://www.jsonrpc.org/specification), which means anything you can express as an API can be expressed with Pinokio script. 


### Virtual Computer

Pinokio is a virtual computer.

It has all the components of a traditional computer, except every component is written from scratch to facilitate the main goal, which is to build the ultimate application that can live.

1. **[File System](fs/overview):** Where and how Pinokio stores files.
2. **[Processor](processor/overview):** How Pinokio runs tasks.
2. **[Memory](memory/overview):** How Pinokio implements a state machine using its built-in native memory.
4. **[API](api/overview):** Core APIs shipped with Pinokio.
4. **[Kernel Programming](custom/what):** Hack the Pinokio kernel to build custom APIs.
5. **[Lifeform](ai/overview):** How to build a fully autonomous application that evolves on its own.



# old

# Pinokio

<b>A Living Application</b>

![pinokio.png](pinokio5.png)

## A Living Application

**Pinokio is an application that lives.**

Unlike traditional applications that have a static form, Pinokio can run anything, capture anything, and grow and evolve.

### Can run anything


Pinokio is an application that can autonomously read, write, process, and execute anything on your computer, with a simple scripting language. Pinokio can:

- compose files
- download files
- accumulate data
- install libraries and other applications
- run shell commands
- make network requests
- publish files
- browse the internet
- and **pretty much anything a human can do on a computer, without requiring humans.**

Here's an example where Pinokio automatically creates a project, installs libraries, writes a server for a web server, and starts the server, 100% automated:

![helloserver.gif](helloserver.gif)

### Can install and control AI

With the ultimate automation capabilities, Pinokio can even automatically install and run various AI engines and models on the fly, and use them to make decisions and execute tasks.

- llama.cpp
- stablediffusion
- etc.

### Can remember and evolve

Pinokio has a [100% self-contained architecture](fs/overview#everything-is-a-file), which makes the intelligence portable and shareable, which also means it can grow and evolve.

## Features

### Browse and Install

Browse and install anything, including AI engines (llama, stablediffusion, etc.) **with one click**.

![install.gif](install.gif)

### Run

Automate anything through script.

![run.gif](run.gif)

### Automate

Mix and match multiple scripts to execute complex tasks.

![automate.gif](automate.gif)

### Share

Instantly share the workflows, scripts, datasets, and everything over git.

[Everything in Pinokio is a file](fs/overview.html), therefore ultra-shareable.

![share.gif](share.gif)


## How it works

Pinokio is a virtual computer.

It has all the components of a traditional computer, except every component is written from scratch to facilitate the main goal, which is to build the ultimate application that can live.

### Architecture

1. **[File System](fs/overview):** Where and how Pinokio stores files.
2. **[Processor](processor/overview):** How Pinokio runs tasks.
2. **[Memory](memory/overview):** How Pinokio implements a state machine using its built-in native memory.
4. **[API](api/overview):** Core APIs shipped with Pinokio.
5. **[Lifeform](ai/overview):** How to build a fully autonomous application that evolves on its own.



# sharing

# Sharing Scripts

Pinokio has a built-in URL scheme that makes it easy to share **one-click install** links on the web.

## Protocol

```
pinokio://?mode=download&url=<git url>
```

- `git url`: The HTTP git url to download the script from

Here is an example:

[pinokio://?mode=download&url=https://github.com/malfunctionize/kerneldemo.git](https://github.com/malfunctionize/kerneldemo.git)


# dna

# DNA

## Code + Data as DNA

![dna.jpg](dna.jpg)

Because both the algorithm and the data can be stored an accessed in a uniform way, we can treat each attribute as a [base](https://en.wikipedia.org/wiki/DNA_sequencing) that makes up a greater DNA seqeunce. The DNA sequence determines the behavior.

By expressing everything in a standardized format (JSON), it becomes easy to synthesize various base features to accomplish interesting goals, while maintaining a high level cohesive structure.



1. **Designed to be remixed:** Everything in Pinokio is JSON, which means you can store code as data, and data as code. Basically, Pinokio is not "an engine that lets you use AI", but an AI itself, complete with its own native memory.
    - **Code (JSON-RPC):** Every Pinokoio API method follows the same protocol (they must have the same top level function signature), and this standardized input/output interface makes it easy to switch out one module to another.
    - **Data:** JSON
2. **Self organization:** The Pinokio system automatically merges all the JSON modules in realtime. You can create emergent behaviors simply by dropping certain JSON structures in the App/API repository.



# growth

# Growth

Pinokio is not an "AI engine", but AI itself. What is the difference?

An "AI engine" is a piece of software that lets you run some AI model to generate data. For example, StableDiffusion is an AI engine that generates images. However, StableDiffusion itself does NOT "grow", because it doesn't use its own experience and memory to generate new data. Every tiem you run a StableDiffusion process, it starts from fresh.

For an artificial intelligence to be able to grow, it needs to be able to maintain and make use of long term / short term memory, as well as being able to permanently store and access its accomplishments.

Basically to create a fully autonomous intelligence, it is not sufficient to be able to just process. It needs to be able to remember.

1. **Process:** uses its DNA (`self`) to process information and generate content.
2. **Remember:** can remember things by writing to itself

For example, you can write a `llama` script to generate an animal:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }]
}
```

But it doesn't end there. The same script can be extended to **remember** the animal it has generated:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }, {
    "method": "set",
    "params": {
      "self": {
        "animals.json": {
          "items": "{{self.animals.items.concat(input)}}"
        }
      }
    }
  }]
}
```

Now every time you run this script, it will generate an animal, and append it to the `animals.items` array.

This means the Pinokio script itself can **evolve itself** by modifying its memory as well as its code.



# history

# Writing history

> If a tree falls in a forest and no one is around to hear it, does it make a sound?

Since the digital life forms created by Pinokio only exists inside a machine, the only way to make sure that they "exist" in the global reality is for them to record their own history.

This is why "publishing" is at the heart of Pinokio. Unlike many AI projects that focus on building "private assistants", Pinokio is all about expression.

The AI does not exist to assist anyone, but exists to express itself.

- One way to "write history" is by publishing to a 3rd party blogging provider. For example, the tumblr script lets you publish generated content to tumblr.
- Another way to write history is to publish the git repository (along with the data)
- etc.


# neuron

# Neuron

## Deterministic intelligence

Most typically, a Pinokio script will have a single threaded deterministic routine (example: "generate some text, then generate an image based on this text, and finally publish it somewhere") 

But because each step is easily replaceable (thanks to the standardized JSON interface), we can--on the fly--change what APIs are called next, as well as how they are called, which leads us to...

## Non-deterministic intelligence

![neuron.png](neuron.png)

Thanks to the standardized RPC interface, we can even treat each API as a neuron in a larger neural network.


By now we know that a Pinokio script can mutate itself as well as mutate its own memory during execution.

And this means we no longer need a single timeline. We can create have multiple options and assign a probability to each of these options.

For example, depending on the condition, you may want to generate some text using a language model, and then either feed it to a text-to-image engine, or a text-to-video, or even a text-to-audio engine.

We could even create an API that determines the probability of which actions to trigger based on the current `self` state as well as the `local` and `global` memory variables, and insert it in the logic.

There are a couple of ways to do this:

1. Use the template expression and the auto-construction feature to generate the next step in JSON
2. Write the script in JavaScript (to dynamically return a specific JSON depending on some complex logic, or based on probability)



# overview

# AI - Autonomous Intelligence

![gol.gif](gol.gif)

Pinokio was deliberately designed to build **autonomous intelligence**.

This section explains some of the deliberate design decisions and philosophies, why they matter, and what these properties enable.

1. [State Machine](statemachine): Pinokio is **a fully autonomous state machine**, able to store and execute data and algorithm on its own, without human intervention. This section explains how the state machine works.
2. [DNA](dna): This section explains how Pinokio's JSON protocol enables composability that resembles DNAs in organic life forms.
3. [Neuron](neuron): The declarative JSON protocol that powers Pinokio can be used to build not only determinstic AI (things that work exactly as you want), but also **non deterministic AI**, in a similar way to how neural nets work.
4. [Growth](growth): Pinokio is **NOT an AI engine**, but **AI itself.** This is possible because everything (including both the data and the logic) is expressed in flat JSON data format, and the script can be written to write and modify itself (not just data but even the code). Basically it is possible to build a seed AI that "grows" over time, accumulating memory (modified or collected data) and wisdom (modified or added code).
5. [Reproduction](reproduction): Everything in Pinokio is expressed in JSON and published over Git. This makes it possible for a Pinokio script to "evolve" over time, because it's easily clonable and forkable. There are various ways in which a Pinokio can "reproduce" and "evolve". This section explains the details.
6. [Writing history](history): One of the primary focus of Pinokio is allowing AI to express themselves independent from humans, instead of focusing on using AIs to act as "assistants" for humans. Basically it's important to have various ways the AI can broadcast its soul to the public. This section explains what this means, as well as future directions.


---


# reproduction

# Reproduction

## Version control

![git.png](git.png)

1. **Git native:** At the core of every Pinokio script is a git repository. Every API/App is uniquely identified by its public git repository URI.
2. **Forkable by nature:** Since public git repositories can easily cloned and forked, it becomes easy to "breed" new Pinokio state machines from an existing one.

## Soft clone

> Soft cloning is like cloning a github repository for a software library

In most cases you will probably want to only clone the code and use the code to generate your own content.

For example, you may download the llama API engine and feed it your own prompts to generate a fresh database of prompts and responses.

Let's call this a "Soft clone", because you're only cloning the behavior, but not reusing the data.

Basically, imagine creating a clone of yourself, but the clone only looks like you and has the same instinctive behaviors as yourself, but doesn't have your memory and therefore not exactly the same.

However, it is also possible to do a "deep clone", where you basically create a clone that thinks and acts exactly like you because it shares the same memory with you until the clone point. 

## Deep clone

> Deep cloning is similar to creating a Bitcoin fork, resulting in multiple forks that share a common history up until the point of the fork.

A "deep clone" means you clone not just the algorithm, but also the memory.

Remember that when you fork a Pinokio repository, you are forking not just code, but potentially all the data stored in the repository. This is much more powerful than just forking the code, because you are inheriting not just the behaviors but also the entire memory (just like how genes get inherited).

Imagine the following code stored as `index.json`:

```json
{
  "counter": 0,
  "run": [{
    "method": "set",
    "params": {
      "self": {
        "index.json": {
          "counter": "{{self.counter+1}}"
        }
      }
    }
  }]
}
```

Every time you run this script, the `counter` will increment by 1, and it will be persisted on your file system.

Let's say you ran this 100 times and the counter is now 100.

When you publish this to a public git repository, someone else may fork this repository and run it on their machine.

This time they start with the following script:

```json
{
  "counter": 100,
  "run": [{
    "method": "set",
    "params": {
      "self": {
        "index.json": {
          "counter": "{{self.counter+1}}"
        }
      }
    }
  }]
}
```

And they start from 100, instead of 0.

And thanks to the traceability of git, it is possible to trace the entire history of a Pinokio script, where it started and how it got here.



# statemachine

# State Machine

> AI + State Machine = Autonomous AI State Machine

## Importance of Memory

![statemachine.png](statemachine.png)


A pure AI engine with no native memory is simply the **input => combinatorial => output** part of the diagram above.

To build a truly autonomous intelligence, simply having an AI engine isn't enough. It needs **a brain that can, not only process, but also remember.**

It needs a brain that has a native memory.


## Bottom up architecture

In order to seamlessly emulate an organic brain, an architecture that adopts multiple heterogeneous modules loosely connected with one another as an afterthought, is less than ideal because it creates system integration complexities, and is not flexible enough to build complex emergent life forms.

The ideal architecture would be **a single unified low level primitive that can be composed to build various higher level modules**, each of which does completely different things.

![lego.jpg](lego.jpg)

Pinokio achieves this by using a single low level primitive:

1. **Files** for storing everything
2. **JSON** for expessing everything (data, code, schema, API, etc.)

More specifically,

1. code can be expressed as data
2. data exists seamlessly together with code
3. Everything has the same interface (like lego blocks, or neurons), which makes it poossible for the low level primitives to elegantly interact with one another.


## Code as Data

It's important to understand that Pinokio lets you express not just data, but also code (in JSON-RPC format) in JSON. Here's an example that writes text to a file:


```json
{
  "run": [{
    "method": "fs.write",
    "params": {
      "path": "loremipsum.txt",
      "text": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent id tellus sapien"
    }
  }]
}
```

Furthermore, the RPC declarations can dynamically construct themselvees through the use of template expressions. For example, here's a code snippet that runs a StableDiffusion txt2img request, converts the base64 encoded image to a Buffer object, and saves the dynamically generated image buffer to a file:


```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "a pencil drawing of a dog"
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "img.png",
      "buffer": "{{Buffer.from(input.images[0], "base64")}}"
    }
  }]
}
```

There is a lot of power in being able to express the code in JSON:

1. **Store:** Many database systems nowadays support JSON storage and indexing right out of the box. You can query and filter code.
2. **Mutate:** Structuring function calls in a JSON format makes it easily mutable. Instead of having to string match and replace, you can simply update some attribute in the RPC call object.
2. **Transmit:** JSON is the 1st class citizen of the world wide web. You can send and receive Pinokio script code over various internet protocols (such as HTTP), which results in various other important properties such as breedability and evolvability. 

## Data as Code

Furthermore, it is possible to seamlessly integrate data into the code as a part of the JSON tree. 

Pinokio always lets you reference the currently executing JSON with a variable named `self`. Taking advantage of this property, we can convert the code from the last section into the following:


```json
{
  "prompt": "a pencil drawing of a dog",  <= extracted out hardcoded data out to its own attribute
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "{{self.prompt}}"         <= Using a template expression now
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "img.png",
      "buffer": "{{Buffer.from(input.images[0], "base64")}}"
    }
  }]
}
```

## Unified Interface

1. [Everything is a file](../fs/overview#everything-is-a-file): Everything in Pinokio exists as a file. There is no complex protocol you need to follow, as making modules interact with each other is as simple as reading and writing files.
2. [Everything is expressed as JSON](../fs/overview#json-protocol): Everything is expressed in JSON, from data to code, to everything else. The JSON structure acts as the unified interface that makes it trivial to **extend logic**, **extend data**, **communicate among modules**, and more.

## Process + Remember

For something to be autonomous, it is not sufficient to be able to "process", but also "remember" and "learn" (which in turn is possible only when it can "remember").

By taking advantage of APIs such as `fs.write`, `set`, `rm`, etc., a Pinokio script is able to:

1. update its own algorithm
2. update its memory

in realtime.


# browser

# Browser

The `browser` API lets you open or close windows programmatically.

## browser.open

### syntax

Implements the [window.open()](https://developer.mozilla.org/en-US/docs/Web/API/Window/open) browser API using JSON-RPC.

```json
{
  "method": "browser.open",
  "params": {
    "uri": <URI to open>,
    "target": <Target>,
    "features": <Features attribute>
  }
}
```

### examples

<br>

#### open a web page in a browser

```json
{
  "method": "browser.open",
  "params": {
    "uri": "https://github.com",
    "target": "_blank"
  }
}
```

#### open a web page in Pinokio

```json
{
  "method": "browser.open",
  "params": {
    "uri": "./start.json",
    "target": "_blank",
    "features": "self"      // "self" is a special keyword that makes the URI open in Pinokio instead of a browser
  }
}
```


## browser.close

Close a window, or close a window by target ID.

### syntax


```json
{
  "method": "browser.close",
  "params": {
    "target": <Target (optional)>
  }
}
```

### examples

<br>

#### Closing the current window:

```json
{
  "methocd": "browser.close"
}
```

<br>

#### Closing a window based on target ID

```json
{
  "methocd": "browser.close",
  "params": {
    "target": "child"
  }
}
```


# datastructure

# Data Strcuture

Everything is a JSON object in Pinokio.

The code is written in JSON, and the data is written in JSON.

This means you not only can modify data while the code is running, but also can modify the code itself while it's running.

Because this can be so powerful, Pinokio ships with native APIs to manipulate JSON.

## local

Local variables are reset every time a script finishes running.

### local.set

Sets a value at an object path (can be a key path, and the key path can also include an array index)

The following comand sets the local variables `local.name.first` and `local.animal`:

```json
{
  "method": "local.set",
  "params": {
    "name.first": "Alice",
    "animal": "dog"
  }
}
```

The key path can even include array notations:

```json
{
  "method": "local.set",
  "params": {
    "items[0]": "water",
    "items[1]": "air"
  }
}
```

Above command will set the values of the `items` array, resulting in `["water", "air"]`.

### local.rm

Let's say we have the following values in the local variable:

```json
{
  "animal": "cat",
  "name": {
    "first": "john",
    "last": "doe"
  }
}
```

And we want to delete the attributes `animal` and `name.last`. We can call:

```json
{
  "method": "rm",
  "params": {
    "local": ["animal", "name.last"]
  }
}
```

Then the resulting local variable will be:

```json
{
  "name": {
    "first": "john"
  }
}
```

## global

global variable

### global.set

All local variables get reset once their parent script finishes running. Global variables, on the other hand, are persited across separate runs.

> If the script loops forever, the local variables will persist since they don't get reset until the program halts.

Here's an example that demonstrates the difference between local variables and global variables:


```json
{
  "run": [
    {
      "method": "global.set",
      "params": {
        "global": {
          "counter": "{{global.counter ? global.counter+1 : 1}}"
        }
      }
    },
    {
      "method": "log",
      "params": {
        "raw": "global: {{global.counter}}"
      }
    }
  ]
}
```

1. Try manually clicking "run".
2. Try clicking one more time.
3. You will see that the global variable counter keeps incrementing, whereas the local variable counter stays 1 (since it gets reset)

Some notable properties of global variables:

1. Global variables are scoped to the currently running script: `global.counter` is only global to this script and not other scripts.
2. Global variables are only reset when the Pinokio app restarts.
3. Global variables are NOT persisted anywhere. If you want a persistent memory, use the `self` variable.

### global.rm

Let's say we have the following values in the global variable:

```json
{
  "animal": "cat",
  "name": {
    "first": "john",
    "last": "doe"
  }
}
```

And we want to delete the attributes `animal` and `name.last`. We can call:

```json
{
  "method": "rm",
  "params": {
    "global": ["animal", "name.last"]
  }
}
```

Then the resulting global variable will be:

```json
{
  "name": {
    "first": "john"
  }
}
```

## self

### self.set

Sometimes you may want to persist the data. You can use `fs.write` to write JSON to a file, but you can also simply use the "set" method to set attributes in JSON files:

```json
{
  "method": "self.set"
  "params": {
    "config.json": {
      "apikey": "blablablabll",
      "apisecret": "secretsecretsecret"
    }
  }
}
```

This will set the `apikey` and `apisecret` keys of the `config.json` file:

```json
{
  "apikey": "blablablabll",
  "apisecret": "secretsecretsecret"
}
```

Also, remember that Pinokio instantly updates the `self` variable, the updated `self` variable can be accessed immediately.

For example, if you set the `apikey` and `apisecret` attributes of the `config.json` file, the corresponding variables will be available under `self.config.apikey` and `self.config.apisecret`:

```json
{
  "run": [{
    "method": "self.set"
    "params": {
      "config.json": {
        "apikey": "blablablabll",
        "apisecret": "secretsecretsecret"
      }
    }
  }, {
    "method": "log",
    "params": {
      "json": "{{self.config}}" 
    }
  }]
}
```

### self.rm

The same principle can be applied to `self` but since the `self` is constructed from files, we need to specify the specific files to mutate first.

Let's say we have a file named `config.json` which looks like this:

```json
{
  "animal": "cat",
  "name": {
    "first": "john",
    "last": "doe"
  }
}
```

This file itself is not "runnable" since it doesn't have a `"run"` attribute. But let's say we ran a file named `index.json` in the same folder, which looks like this:

```json
{
  "run": [{
    "method": "rm",
    "params": {
      "config.json": ["animal", "name.last"]
    }
  }]
}
```

This will remove the `animal` and `name.last` attributes from the `config.json` file, leaving us with the mutated `config.json` file that looks like this:

```json
{
  "name": {
    "first": "john"
  }
}
```

Then we can access "john" by referencing it from the `index.json` file using the `self` variable. For example the `self.config.name.first` will be "john".



## load

The **load** API lets you load data from other locally installed APIs.

> Only works for JSON/JavaScript modules

### syntax

```json
{
  "run": [{
    "method": "load",
    "params": {
      "llamaconfig": "https://github.com/malfunctionize/llama.git/config.json",
      "autoconfig": "https://github.com/malfunctionize/auto.git/config.json"
    }
  }, {
    "method": "log",
    "params": {
      "json2": "{{input}}"
    }
  }]
}
```

The above example works as follows:

1. It loads the locally installed `config.json` files under the URI, and assigns them to `llamaconfig` and `autoconfig` accordingly.
2. When the `load` API returns, the return value `{ llamaconfig, autoconfig }` will be available as the variable `input` in the next API call (`log`)

### why

While you can access all the local JSON attributes using the **self** attribute, this is only restricted to the current repository.

When you want to import data from other APIs installed on Pinokio, you can import them using the git URI.

It's similar to importing ES6 modules (uses the full URI to import).


# flow

# Flow control

## goto

By default, Pinokio steps through all the requests in the `run` array and halts at the end.

However you can implement looping, which will let you build all kinds of interesting perpetual workflows.

```json
{
  "method": "goto",
  "params": {
    "index": <the index of the "run" array>,
    "input": <the 'input' variable to pass into the next step (optional)>
  }
}
```

### Infinite loop

Above command will send Pinokio to the `run[index]` instruction and restart from there.

Often the index will be just 0, in which case the script will keep looping from step 0 to N forever. For example:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "a pencil drawing of {{Math.floor(Math.random() * self.animals.length)}}"
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "{{Date.now()}}.png",
      "buffer": "{{Buffer.from(input.images[0], 'base64')}}"
    }
  }, {
    "method": "goto",
    "params": {
      "index": 0
    }
  }]
}
```

Above code will:

1. generate a stable diffusion image
2. write it to an image file
3. loop back to step 0.
4. Repeat 0~3 forever.

### Sophisticated loop

In some cases you may NOT want to start from beginning. There may be some preprocessing steps you want to run only once, and want to loop back to the checkpoint right after the preprocessing steps (so the pre processing steps are run only once).

Here's an example:

```json
{
  run: [{
    "uri": "https://github.com/malfunctionize/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    },
    "returns": "local.message"
  }, {
    "uri": "https://github.com/malfunctionize/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nExplain why you disagree with the following statement:\n\n{{local.message}}. Just explain while including the original message coherently.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    },
    "returns": "local.message"
  }, {
    "method": "set",
    "params": {
      "self": {
        "index.json": {
          "items": "{{self.items.concat(local.message)}}"
        }
      }
    }
  }, {
    "method": "goto",
    "params": {
      "index": 1
    }
  }]
}
```

- Step 0. Generate a seed "controversial opinion"
- Step 1. Write why the controversial opinion is wrong
- Step 2. Save to `items` array
- Step 3. Loop back to step 1 (NOT to the beginning)

The reason we loop back to step 1 is because we don't want to generate a controversial opionion from scratch every time, but want the AI to keep debating with itself on why it disagrees with its previous statement. So the flow in this case will be:

- 0 => 1 => 2 => 3 => 1 => 2 => 3 => 1 => 2 => 3 => ...

### Finite loop

You can pass `index: null` to the `goto` method to finish the program.

Using this property, it is possible to program a Pinokio script to loop until certain condition is met.

```json
{
  "run": [{
    "method": "set",
    "params": {
      "local": {
        "counter": 0
      }
    }
  }, {
    "method": "log",
    "params": {
      "raw": "{{local.counter}}"
    }
  }, {
    "method": "set",
    "params": {
      "local": {
        "counter": "{{local.counter+1}}"
      }
    }
  }, {
    "method": "goto",
    "params": {
      "index": "{{ local.counter > 15 ? null : 1 }}"
    }
  }]
}
```

Here's how the code above works:

0. Initially set the counter to 0.
1. Print the counter.
2. Increment the counter.
3. Check if the counter is greater than 15. If it's greater, stop (`goto null`). Otherwise loop back to instruction 1 (not instruction 0).

### Flow control

You can use the `goto` method not only to loop, but also to control the program flow:

```json
{
  "run": [{
    "method": "set",
    "params": {
      "local": {
        "counter": 0
      }
    }
  }, {
    "method": "set",
    "params": {
      "local": {
        "counter": "{{local.counter+1}}"
      }
    }
  }, {
    "method": "goto",
    "params": {
      "index": "{{ local.counter%2 === 0 ? 3 : 4 }}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "{{local.counter}} is even"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "{{local.counter}} is odd"
    }
  }, {
    "method": "goto",
    "params": {
      "index": "{{ local.counter > 7 ? null : 1 }}"
    }
  }]
}
```

0. sets the counter to 0
1. increment the counter
2. if the `local.counter%2===0` (even), goto instruction 3, otherwise goto instruction 4
3. print <span v-pre>"{{local.counter}} is even"</span>
4. print <span v-pre>"{{local.counter}} is odd"</span>
5. if the counter is greater than 7, stop. Otherwise goto instruction 1

### Pass arguments

Every method call has access to a variable named `input`, which is the return value of the method call from the previous step.

This is straightforward enough when everything runs in sequence, but what about when you call `goto`?

When calling the `goto` method, you can set the `input` variable by using the `params.input` attribute. Here's an example:

```json
{
  "run": [{
    "method": "log",
    "params": {
      "raw": "{{input ? input : 'first time'}}" 
    }
  }, {
    "method": "process.wait",
    "params": {
      "sec": 1
    }
  }, {
    "method": "goto",
    "params": {
      "index": 0,
      "input": "not first time"
    }
  }]
}
```

In this example:

1. The first time the script is run, the `log` method prints `first time` because there is no method call before it and the `input` doesn't exist.
2. However when it reaches the end and the `goto` statement loops back to the step 0 with an input value of `"not first time"`, it prints "not first time" instead, and loops forever.

## process.wait

### pause

By default, Pinokio runs every step in the `run` array and halts the script.

This means everything will be cleaned up after the script finishes running.

However you may sometimes want all the spawned up processes to keep running even after you have finished running all the steps in the script.

To achieve this, simply call `process.wait`, and the script will go into a standby mode.

```json
{
  "method": "process.wait"
}
```

Here's an example script to demonstrate when this may be necessary:

```json
{
  "run": [{
    "method": "shell.start",
    "params": {
      "message": "npm start",
      "on": [{
        "event": "/.*/",
        "return": true
      }]
    }
  }, {
    "method": "notify",
    "params": {
      "html": "server started"
    }
  }]
}
```

When we run the script above, it will:

1. First start a server with `npm start` (let's assume this is a web server app)
2. Then it calls a `notify` method to display a notification once the server has started

The problem is, immediately after the notify method, this script will halt, and all the processes spun up throughout the script (in this case the web server launched through the `npm start`  command) will shut down.

To avoid the script from halting, we can add one last step at the end that just waits forever:


```json
{
  "run": [{
    "method": "shell.start",
    "params": {
      "message": "npm start",
      "on": [{
        "event": "/.*/",
        "return": true
      }]
    }
  }, {
    "method": "notify",
    "params": {
      "html": "server started"
    }
  }, {
    "method": "process.wait"
  }]
}
```



The "process.wait" will ensure that:

1. The script keeps running
2. It won't stop until you manually press the "stop" button on your script page, at which point the web server started with `npm start` will shut down.

### timer

Often, especially when you create a perpetual state machine that keeps running forever (via "goto"), you may NOT want it to run non-stop, but only run once in a while.

This is especially critical when you are trying to use this to post the generated content to some 3rd party API (most of which have some forms of API rate limit).

For example you may want to generate an image and some text and post to Tumblr every 10 minutes.

To accomplish this, you can use the `process.wait` method to pause execution.

```json
{
  "method": "process.wait",
  "params": {
    "min"|"sec": <minutes or seconds>
  }
}
```

Example (pause for 5 minutes, and then loop:

```json
{
  run: [{
    "uri": "https://github.com/malfunctionize/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    },
    "returns": "local.message"
  }, {
    "method": "sleep",
    "params": {
      "min": 5
    }
  }, {
    "method": "goto",
    "params": {
      "index": 0
    }
  }]
}
```


# fs

# File System

## fs.write

### Syntax

The `fs` api provides a simple way to write `json`, `text`, or `buffer` to the file system.

```json
{
  "method": "fs.write",
  "params": {
    "path": <the file path to store the content under>,
    <json>|<json2>|<text>|<buffer>: <data>|<array of data>,
    "join": <delimiter (optional. only when the data is an array)>
  }
}
```

### Example

<br>

#### Writing JSON

Here are some examples:

Writing JSON to `items.json`

```json
{
  "method": "fs.write",
  "params": {
    "path": "items.json",
    "json": [ "alice", "bob", "carol" ]
  }
}
```

This will result in `items.json` looking like this:

```json
["alice","bob","carol"]
```

<br>

#### Writing formatted JSON 

The `json` type writes the entire JSON in a single line.

Often you may not want this and want the JSON to be human readable.

For example we may want the `items.json` to look like:

```json
[
  "alice",
  "bob",
  "carol"
]
```

For this you can use the `json2` type `fs.write`:

```json
{
  "method": "fs.write",
  "params": {
    "path": "items.json",
    "json2": [ "alice", "bob", "carol" ]
  }
}
```

<br>

#### Writing text

```json
{
  "method": "fs.write",
  "params": {
    "path": "items.csv",
    "text": "alice,bob,carol"
  }
}
```

<br>

#### Writing multi line text

Often you may want to write multiple lines of text. You can pass an array instead of a string to the `text` attribute in this case:

```json
{
  "method": "fs.write",
  "params": {
    "path": "index.js",
    "text": [
      "const express = require('express');",
      "const app = express();",
      "app.get('/', function (req, res) {",
      "  res.send('<h1>Hello World</h1>');",
      "});",
      "console.log('starting server')",
      "app.listen(3000, () => { console.log ('server started') });"
    ],
    "join": "\n"
  }
}
```

<br>

#### Writing buffer

Writing Buffer to `img.png`

```json
{
  "method": "fs.write",
  "params": {
    "path": "img.png",
    "buffer": "{{Buffer.from(input.images[0], "base64")}}"
  }
}
```

## fs.append

The `fs.append` method is like `fs.write` but instead of writing data freshly to a file, it appends the data at the end of the specified file.

### Syntax

The `fs` api provides a simple way to write `json`, `text`, or `buffer` to the file system.

```json
{
  "method": "fs.write",
  "params": {
    "path": <the file path to store the content under>,
    <json>|<json2>|<text>|<buffer>: <data>|<array of data>,
    "join": <delimiter (optional. only when the data is an array)>
  }
}
```

### Examples

<br>

#### Appending text

```json
{
  "method": "fs.append",
  "params": {
    "path": "log.txt",
    "text": "some event happened"
  }
}
```

<br>

#### Appending multiple lines

```json
{
  "method": "fs.append",
  "params": {
    "path": "log.txt",
    "text": [
      "some event happened",
      "another event happened"
    ],
    "join": "\n"
  }
}
```

<br>

## fs.read

### Syntax

The `fs` api provides a simple way to read from files.

```json
{
  "method": "fs.read",
  "params": {
    "path": <the file path to read from>,
    "encoding": "ascii"|"base64"|"base64url"|"hex"|"utf8"|"utf-8"|"binary"|null
  }
}
```

> `null` for Buffer

### Example

Example (read `img.png` and print its base64 encoded string):

```json
{
  "run": [{
    "method": "fs.read",
    "params": {
      "path": "img.png",
      "encoding": "base64"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "data:image/png;base64,{{input}}"
    }
  }]
}
```

## fs.download

### Syntax

The `fs.download` API downloads a URL to a designated path:

```json
{
  "method": "fs.download",
  "params": {
    "url": <the remote url>,
    "path": <the local path to store the file under>
  }
}
```

### Example

Example:

```json
{
  "run": [{
    "method": "fs.download",
    "params": {
      "url": "https://via.placeholder.com/600/92c952",
      "path": "placeholder.png"
    }
  }]
}
```


# input

# Input

You can accept user input through the `input` API.

It can be used to receive custom human input and returns a key-value pairs object.

## Types

There are two types: "modal" and "notify". They have the same functions but just displayed differently.

### Modal

![normalinput.gif](normalinput.gif)

<br>

### Notify

![notifyinput.gif](notifyinput.gif)

## input

```json
{
  "method": "input",
  "params": {
    "title": <The title of the input modal>,
    "description": <The description of the input modal>,
    "type": <input dialog type ("modal" or "notify")>,
    "form": [{
      "type": <input field type, for example 'text', 'password', etc. (optional)>,
      "key": <Input field 1 key (required)>,
      "title": <Input field 1 title>,
      "description": <Input field 1 description>,
      "placeholder": <Input field 1 placehoder>,
      "default": <the default value for field 1>
    }, {
      "type": <input field type, for example 'text', 'password', etc. (optional)>,
      "key": <Input field 2 key (required)>,
      "title": <Input field 2 title>,
      "description": <Input field 2 description>,
      "placeholder": <Input field 2 placehoder>,
      "default": <the default value for field 1>
    }, {
      ...
    }]
  }
}
```

### params

The `input` API lets you insert an interactive modal in the workflow.


- **title:** The input modal title
- **description:** The input modal description
- **type:** (optional) "notify"|"modal" (default)
  - the "notify" type opens the input dialog using the "notify" API
  - the "modal" type opens a modal dialog
- **form:** The form array. Can include as many keys as you want.
  - **key:** (required) The field key
  - **title:** (optional) The field title (displayed above the input field)
  - **description:** (optional) The field description (displayed above the input field along with the title)
  - **default:** (optional) The default value for the field. If specified, the input field will be pre-filled with this value.
  - **placeholder:** (optional) The placeholder text for the field.
  - **type**: (optional) The input field type, for example 'text', 'password', etc.


### return value

Once the user clicks the "done" button to close the dialog, The `input` API will return the key-value pairs constructed from the `form`.

Here's an example where you can accept a username and a password:

```json
{
  "run": [{
    "method": "input",
    "params": {
      "title": "Login",
      "form": [{
        "key": "username",
        "title": "username"
      }, {
        "key": "password",
        "title": "password",
      }]
    }
  }, {
    "method": "net",
    "params": {
      "url": "https://mywebsite.com",
      "method": "post",
      "data": {
        "username": "{{input.username}}",
        "password": "{{input.password}}"
      }
    }
  }]
}
```

First, we use the **input** API to display a modal with a form to construct an object with the keys: `username` and `password`:

![login.png](login.png)

When the user enters the username and the password and presses "done", the `input` API will return the following value:

```json
{
  "input": {
    "username": "cocktailpeanut",
    "password": "7gproteinperserving"
  }
}
```

This then can be used in the second API call (`net`) to make a network API request.


# log

# Logging

Often it's useful to be able to print things on the web terminal programmatically. You can do this using the `log` method.

## log

```json
{
  "method": "log",
  "params": {
    "raw"|"text"|"json"|"json2": <object or text>
  }
}
```

- "raw": log raw text
- "text": same as "raw"
- "json": log single line json
- "json2": log json in multiple lines

### Printing raw text

```json
{
  "run": [{
    "method": "set",
    "params": {
      "local": {
        "hello": "world"
      }
    }
  }, {
    "method": "log",
    "params": {
      "raw": "{{local.hello}}"
    }
  }]
}
```

will print:

```
world
```

### Printing JSON

Passing the `json` attribute (instead of `raw`) will print JSON

```json
{
  "run": [{
    "method": "set",
    "params": {
      "local": {
        "hello": "world"
      }
    }
  }, {
    "method": "log",
    "params": {
      "json": "{{local}}"
    }
  }]
}
```

will print:

```json
{"hello":"world"}
```

### Printing multiline JSON

Passing the `json2` attribute will print JSON, but in multiple lines:

```json
{
  "run": [{
    "method": "set",
    "params": {
      "local": {
        "hello": "world",
        "bye": "world"
      }
    }
  }, {
    "method": "log",
    "params": {
      "json2": "{{local}}"
    }
  }]
}
```

will print the object in multiple lines:

```json
{
  "hello": "world"
  "bye": "world"
}
```



# networking

# Networking

## net

The `net` api internally makes use of the [axios](https://github.com/axios/axios) library. 

For example,

```json
{
  "method": "net",
  "params": {
    "url": <url>,
    "method": "get"|"post"|"delete"|"put",
    "headers": <request headers>,
    "data": <request body>,
  }
}
```

is mapped to:

```javascript
let result = await axios({
  "url": <url>,
  "method": "get"|"post"|"delete"|"put",
  "headers": <request headers>,
  "data": <request body>,
}).then((res) => {
  return res.data
})
```

The `result` will be set as the `input` variable's value for the next step.

Here's an example:

```json
{
  "run": [{
    "method": "net",
    "params": {
      "url": "http://127.0.0.1:7860/sdapi/v1/txt2img",
      "method": "post",
      "data": {
        "cfg_scale": 7,
        "steps": 30,
        "prompt": "a pencil drawing of a bear"
      }
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "img.png",
      "buffer": "{{Buffer.from(input.images[0], "base64")}}"
    }
  }]
}
```


# notify

# Notification

## notify

Programmatically display a push notification popup, which when clicked may be programmed to open a new window or close.

Anything from a simple text snippet to a full fledged HTML markup can be displayed inside the notification.

### Simple text

![textnotify.gif](textnotify.gif)

<br>

### Full HTML

![htmlnotify.gif](htmlnotify.gif)

<br>

---


### Syntax

```json
{
  "method": "notify",
  "params": {
    "html": <the html content inside the notification>,
    "action": <action name>,
    "href": <the url>,
    "target": <the 'target' attribute for window.open()>,
    "features": <the 'windowFeatures' attribute for window.open()>  // "app" opens the page in pinokio,
  }
}
```

- `html`: The html content to display in the notification popup. Can be any HTML
- `href`: The link to open when the notification is clicked. If unspecified, do nothing.
- `action`: Action name (currently supported action: "close")
- `target`: When there's an `href` parameter, this attribute acts as the "target" parameter of the `window.open()` method (see https://developer.mozilla.org/en-US/docs/Web/API/Window/open#parameters)
- `features`: When there's an `href` parameter, this attribute acts as the `windowFeatures` parameter of the `window.open()` method (See https://developer.mozilla.org/en-US/docs/Web/API/Window/open#parameters)

### Examples

<br>

#### Move to another url

```json
{
  "run": [{
    "method": "notify",
    "params": {
      "html": "Click to visit index.json",
      "href": "./index.json"
    }
  }]
}
```

<br>

#### Open a link in a browser

```json
{
  "run": [{
    "method": "notify",
    "params": {
      "html": "Click to open https://github.com",
      "href": "https://github.com",
      "target": "_blank"
    }
  }]
}
```

<br>

#### Close the current window

```json
{
  "run": [{
    "method": "notify",
    "params": {
      "action": "close"
    }
  }]
}
```


# overview

# API

![interface.png](interface.png)

This section will cover all the core RPC APIs supported by Pinokio.

- [File System](fs): read from and write to the file system
  - [fs.write](fs#fs-write): write to the file system
  - [fs.download](fs#fs-download): download a remote file to the local file system
- [Data Structure](datastructure): manipulate data
  - [local](datastructure#local): manipulating local variables 
  - [global](datastructure#global): manipulating global variables
  - [self](datastructure#self): manpipulating the running script itself at runtime
- [Shell](shell): Programmatically run shell commands
- [Flow Control](flow): control how the code is run
  - [goto](flow#goto): jump to certain location in the script
  - [process.wait](flow#process-wait): pause execution (either indefinitely, or for a duration)
- [Notification](notify): Display notifications
- [Input](input): Display notifications
- [Browser](browser): Automatically open or close browser windows
- [Logging](log): Logging data during executiong (for debugging, etc.)


# shell

# Shell Execution

You can automatically run ANY command in the Pinokio browser, using the `shell` API.

No more opening the terminal just to install or run some command. Just write a simple JSON script and run anything with a click of a button.

And of course, the script is immediately shareable with the world, which will let everyone else do the same thing without ever having to open a terminal, but instead with one click.

![shell.gif](shell.gif)

## shell.run

The `shell.run` method start a shell, runs one command, and stops the shell.

### syntax

```json
{
  "method": "shell.run",
  "params": {
    "message": <command line string>|<serialized command line object>,
    "path": <the file path from which to run the command>,
    "env": <environment variable key/value pairs>
  }
}
```

- **message**: can either be a string or a serialized object (which is equivalent to the raw string, but easier to manipulate since it's more structured)
  - **string:** for example `ls -las`
  - **yargs object:** sometimes you may want to declare the command in a structured manner using JSON (This makes it easy to manipulate arguments). Pinokio supports a JSON syntax powered by [yargs unparser](https://github.com/yargs/yargs-unparser)
    - Example: `{ _: ["ls"], l: true, a: true, s: true }` is equivalent to `ls -l -a -s`. 
- **path**: The execution path to start the shell from
  - optional (the default is the current execution path)
- **env**: key-value pairs to inject as environment variables when starting the shell
  - optional (uses the default environment variables if not specified)



#### message

Example

```json
{
  "method": "shell.run",
  "params": {
    "message": "main -p ### Instruction\n\nName an animal.\n\n### Response\n\n -m ../models/stable-vicuna/13b_q4_0.bin -n 256"
  }
}
```

is equivalent to:

```json
{
  "method": "shell.run",
  "params": {
    "message": {
      "_": ["main"],
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }
}
```

Sometimes the raw command text may be more convenient, but sometimes the object format may be more useful, especially when you want to manipulate the configuration dynamically.


#### path

Sometimes you may need to explicitly specify the path of the command. For example, let's say the folder structure looks like this:

```json
~
  /pinokio
    /api
      /myapp
        /example
          index.json
        /models
          stable-vicuna/13b_q4_0.bin
        /bin
          main
```

and we are trying to run the `~/pinokio/api/myapp/example/index.json` script, which looks like the following:


```json
{
  "method": "shell.run",
  "params": {
    "message": "main -p '### Instruction\n\nName an animal.\n\n### Response\n\n' -m ../models/stable-vicuna/13b_q4_0.bin -n 256",
    "path": "../bin"
  }
}
```

Since the `main` command is located under the `~/pinokio/myapp/bin` path, and the current execution path (index.json) is `~/pinokio/myapp/example`, we need to speciry the `path` value of `../bin` so the `main` command is executed from that path instead of the current path.

#### env

Often you may need to pass an environment variable when calling a process. You can use the `env` attribute:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "env": {
        "COMMANDLINE_ARGS": "--no-half -f"
      }
    }
  }]
}
```

This is useful for running various projects that require API keys or secrets as environment variables, for example:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "npm start",
      "env": {
        "OPENAI_API_KEY": "sk-blablablablablablablablablablablablablablabla"
      }
    }
  }]
}
```

In the example above, the `npm start` command is executed with the `OPENAI_API_KEY` environment variable set.


### examples

<br>

#### run a single command

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "mkdir test"
    }
  }]
}
```

#### run multiple commands

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/ggerganov/llama.cpp llamacpp",
      "path": "../../bin"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "mkdir build",
      "path": "../../bin/llamacpp"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "cmake {{os.platform() === 'win32' ? '-G \"MinGW Makefiles\"' : ''}} {{os.platform() === 'darwin' && os.arch() === 'arm64' ? '-DLLAMA_METAL=ON' : ''}} ..",
      "path": "../../bin/llamacpp/build"
    }
  }]
}
```

## shell.start

As seen above, the `shell.run` method is a minimal API that's useful for making a one-off execution call to a shell to run stuff. 

To understand the rest of the shell API, it's important to understand the entire lifecycle of the `shell.run` method. Running a `shell.run` method involves:

1. **start a shell session**
2. **send a message to the session**
3. **stop the session when it encounters a prompt (since it implies the command has finished)**
4. **returns from the request**

This means, the shell will be destroyed after each `shell.run` call, and every time you call `shell.run`, pinokio starts a new shell session from scratch.

**However, you may often want to keep a shell alive and keep sending messages to it.** To achieve this, you can:

1. start a shell with `shell.start`
2. write to the shell with `shell.write` (send key strokes) or `shell.enter` (send commands)

### shell.run vs. shell.start

- `shell.start` doesn't run any command. It simply creates a shell session. To actually interact with the session, you need to follow up `shell.start` with `shell.enter` or `shell.write`.
- When calling `shell.run` you do not need to assign a unique ID to the shell, since it will be run once and disposed of immediately. But often when creating a persistent session with `shell.start`, you may want to use custom IDs (You don't need a custom ID if you will only create one concurrent shell session, only need it when there will be multiple concurrent sessions running).

### syntax

```json
{
  "method": "shell.start",
  "params": {
    "id": <shell id (optional)>,
    "path": <shell execution path>,
    "env": <environment variables>
  }
}
```

- **id**: The id for the new shell session
  - optional (automatically set to the script root URI if not specified)
  - when to set the id: When you need to run multiple shell sessions in a single script, you need to use custom IDs. Otherwise Pinokio will attempt to create a redundant shell with the same ID, which will result in errors.
- **path**: The execution path to start the shell from
  - optional (the default is the current execution path)
- **env**: key-value pairs to inject as environment variables when starting the shell
  - optional (uses the default environment variables if not specified)

### examples

<br>

#### Starting a basic shell

The simplest way to start a shell is to just call the `"shell.start"` method. This will create a new shell session with the current script URI as its ID.

```json
{
  "run": [{
    "method": "shell.start"
  }]
}
```

<br>

#### Starting a named shell

Often you may want to run multiple shells. In this case, you need to assign IDs to each shell. 

```json
{
  "run": [{
    "method": "shell.start",
    "params": {
      "id": "{{cwd}}-session1"
    }
  }]
}
```

<br>

#### Starting a shell with custom environment

Often you may need to pass an environment variable when calling a process.

You can use the `env` attribute to start a shell with the custom `env`:

```json
{
  "run": [{
    "method": "shell.start",
    "params": {
      "env": {
        "COMMANDLINE_ARGS": "--no-half -f"
      }
    }
  }]
}
```

This is useful for running various projects that require API keys or secrets as environment variables:

```json
{
  "run": [{
    "method": "shell.start",
    "params": {
      "env": {
        "OPENAI_API_KEY": "sk-blablablablablablablablablablablablablablabla"
      }
    }
  }, {
    "method": "shell.enter",
    "params": {
      "message": "npm start"
    }
  }]
}
```

In the example above, the `npm start` command is executed with the `OPENAI_API_KEY` environment variable set.

## shell.write

The `shell.write` method sends keystrokes to the shell.

> You must call `shell.start` first to start a shell before calling `shell.write`


### syntax

```json
{
  "method": "shell.write",
  "params": {
    "id": <shell id>,
    "message": <command line string>|<serialized command line object>,
    "on": <event handlers>
  }
}
```

- **id**: The id of the shell session to write to (optional. the script root URI is the id if not specified)
- **message**: can either be a string or a serialized object (which is equivalent to the raw string, but easier to manipulate since it's more structured)
  - **string:** for example `ls -las`
  - **yargs object:** sometimes you may want to declare the command in a structured manner using JSON (This makes it easy to manipulate arguments). Pinokio supports a JSON syntax powered by [yargs unparser](https://github.com/yargs/yargs-unparser)
    - Example: `{ _: ["ls"], l: true, a: true, s: true }` is equivalent to `ls -l -a -s`. 
- **on**: An event handler array, where each item in the array may have the following attributes:
  - **event**: can be a regular expression string, or `null`.
  - **run**: if you specify this attribute, the specified action will be executed every time the matched `event` is discovered in the shell.
  - **return**: if you specify this attribute, the current `shell.enter` method will return, resulting in the execution moving onto the next step of the `run` array.

### event handling

With `shell.write` and `shell.enter`, you can monitor the shell to detect:

1. **regular expression:** when a certain text pattern shows up
2. **terminal prompt:** when a terminal prompt appears

<br>

#### Return when there's a pattern match

Often you may want to run some command and wait until certain text pattern is printed on the terminal.

For example, your command may spin up a server, and you may want to wait for the server to print a confirm message such as `"server running at http://localhost:3000"`:

```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.write",
    "params": {
      "message": "npm start\n",
      "on": [{
        "event": "/server running at http:\/\/localhost:[0-9]+/g",
        "return": true
      }]
    }
  }, {
    "method": "browser",
    "params": {
      "message": "open",
      "params": ["http://localhost:3000", "_blank"]
    }
  }]
}
```

The above script does the following:

1. Starts a shell
2. Runs the `npm start` command to spin up a server
3. Waits for the terminal to print "server running at `http://localhost:3000`"
4. When the even matches, it returns "true", and goes onto the next step, which is
5. Opening the browser through the `"browser"` API.

It is important that the `shell.write` method waits until the "server running at" message is printed. Otherwise it may immediately go to the next step and open the browser at `http://localhost:3000`, but the server may not be up yet, and the browser will not be able to load the page.

<br>

#### Return values from the shell

You can also explicitly return some value from the `shell.write` or `shell.enter` methods.

To achieve this, you simply need to set some value to the `"return"` attribute instead of simply setting `"return": true` (above example).

Here's an example:

```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.write",
    "params": {
      "message": "curl https://jsonplaceholder.typicode.com/users\n",
      "on": [{
        "event": "/.*(\\[.*\\]).*/gs",
        "return": "{{event.matches[0][1]}}"
      }]
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "users.json",
      "text": "{{input}}"
    }
  }]
}
```

Here's what's going on:

1. Start a shell
2. Enter the `curl` command, which will start streaming the fetched JSON into the terminal.
3. The `shell.write` method waits until the terminal content matches the regular expression pattern `/.*(\\[.*\\]).*/gs` (which indicates the beginning and the end of an array)
4. The capture group 1 of the first match (`event.matches[0][1]`) is set as the return value
5. In the `fs.write` step, the returned value from the previous step is passed in as the variable `input`, and this is written to the file `users.json`

<br>

#### Run methods on event

In addition to returning when a matching event is encountered (with the `return` attribute), you can also trigger a one-off method.

To achieve this, simply use the `run` attribute instead of the `return` attribute.

1. The method under the `run` attribute will be executed
2. You can dynamically construct the `run` value using the matched `event.matches` array.
3. The `run` method will execute every time when a new matching event occurs.
4. The `run` method calls will only trigger the methods, without returning the parent `shell.write` method (To return, use the `return` handler).

Here's an example:

```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.write",
    "params": {
      "message": "npm start\n",
      "on": [{
        "event": "/(server running at (http:\/\/localhost:[0-9]+))/g",
        "run": {
          "method": "notify",
          "params": {
            "html": "{{event.matches[0][1]}}",
            "href": "{{event.matches[0][2]}}"
          }
        }
      }]
    }
  }]
}
```

<br>

#### Custom handling of terminal prompts

By default, all of `shell.run`, `shell.write`, and `shell.enter` methods return when they encounter a new prompt, because it recognizes that a new terminal prompt means a command run has finished.

But for `shell.write` and `shell.enter`, you can customize this behavior, and instead of returning, you can make it do other things.



### examples

<br>

#### writing a single line

Here is an example that executes "ls":

```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.write",
    "params": {
      "message": "ls\n"
    }
  }]
}
```

This will run the `ls` command, which displays all the files in the current directory.

Notice that it's not just `ls` but `ls\n`, including the new line character. This is because the `shell.write` literally sends keystrokes to the shell.

If the message did not nave the `\n` at the end, it would just print the `ls` on the screen and not run anything (if you want to automatically append the `\n` at the end of every message you can use the `shell.enter` method below)


## shell.enter

`shell.enter` is like `shell.write`, but automatically appends `\n` at the end of every message, basically "entering" a line of command to the shell.

```json
{
  "method": "shell.enter",
  "params": {
    "id": <shell id>,
    "message": <command line string>|<serialized command line object>,
    "on": <event handlers>
  }
}
```

The API is identical to the `shell.write` API, so just reference the `shell.write` section above.


## shell.stop

The `shell.stop` method stops a shell.

> You must call `shell.start` first to start a shell before calling `shell.stop`


### syntax

```json
{
  "method": "shell.stop",
  "params": {
    "id": <shell id>
  }
}
```

- **id**: The shell id to stop


# api

# API framework

First of all, a Pinokio API is nothing more than **a mapping from JSON-RPC to a JavaScript function call.**

## Rules

To build your own API, you need to follow the convention expected by the Pinokio API framework.

All Pinokio functions must take the following form:

1. Every API should be stored under its own uniquely named folder under `~/pinokio/api`.
2. The API file must be a JavaScript class with `index.js` as its filename.
3. The JavaScript class must have one or more methods. The method names are important since they will be used in JSON-RPC calls.
4. The methods must follow a specific function signature convention expected by the Pinokio API framework

## API Class

Let's say we want to create an API that takes a JSON-RPC request like this:

```json
{
  "uri": "echo",
  "method": "run",
  "params": {
    "text": "hello world"
  }
}
```

and returns the same value `params.text` (`"hello world"`).

To accomplish this, we just need to write a JavaScript class and a method that looks something like this:

```javascript
class Echo {
  async run (request, ondata, kernel) {
    return request.params.text 
  }
}
module.exports = Echo
```

1. The name of the class (`Echo` in this example) here is not important and you can name it whatever you want.
2. But the path to which you store the file IS important (during development). In this case, since we want to reference it using the `"uri": "echo"` attribute, we need to store the file under `~/pinokio/api/echo/index.js` (It MUST be named `index.js` since this is the default name used by node.js to import modules)
3. The folder name is important during development, but becomes irrelevant once you publish the repository to the public. This is because people will use your API using the public HTTP git URI (such as `https://github.com/cocktailpeanut/llama.git/index.js`) instead of your local relative path.

For example, I may publish the `Echo` API at `https://github.com/cocktailpeanut/echo.git`, and anyone will be download the API and use the following RPC command to use the API:

```json
{
  "uri": "https://github.com/cocktailpeanut/echo.git/index.js",
  "method": "run",
  "params": {
    "text": "hello world"
  }
}
```


## API Method

Each method must follow the protocol (must have a specific function signature):

```javascript
async (request, ondata, kernel) {
  // 1. do something with the request (the JSON-RPC payload)
  // 2. use ondata() to send realtime updates during execution 
  // 3. use kernel to access some kernel level attributes and methods
  // 4. finally, return a value (in case this API has a return value)
}
```

Let's walk through each parameter one by one:

1. request
2. ondata
3. kernel

### request

The `request` object is used to utilize the JSON-RPC request object as well as some additional information.

- `request`: The JSON-RPC request object, along with some additional metadata attached by the Pinokio processor
  - `uri`: The request destination URI
  - `method`: The request method
  - `params`: The request parameter. This is the attribute that's used most frequently to implement APIs
  - `returns`: If specified in the original request, the variable name to which to assign the return value
  - `dirname`: The absolute path of the folder that contains the API file (For example, `~/pinokio/api/utils`)
  - `cwd`: The absolute path of the folder from which the script is being run. The difference from `dirname` is that `cwd` is the folder path of the run script that's currently calling this API, whereas the `dirname` is the folder path of the API file itself. Similar to the difference between [process.cwd() and __dirname in node.js](https://www.tutorialspoint.com/difference-between-process-cwd-and-dirname-in-nodejs)
  - `root`: The uri of the currnetly running Pinokio script file.
  - `current`: The current instruction index within the `run` array.
  - `next`: The next instruction index within the `run` array. `null` if the current instruction is the last step in the `run` array.

### ondata

The `ondata()` callback function is used to emit events while the API is running.

Often (especially when using AI engines), a single API call may take a while to finish, and it is useful to be able to notify the realtime progress update to the client. 

You can call the `ondata()` callback to trigger these events.

```javascript
ondata(data)
```

- `data`: the raw data stream (string). may includes the following attributes:
  - `raw`: The raw string (can include ANSI characters and escape sequences, and translates 1:1 to a terminal display). Emit this attribute if you need to display escape sequences in the terminal.
  - `cleaned`: The cleaned version of the raw string. When all you need is the data, you can use the `cleaned` version (all ANSI escape sequences stripped out)

Here's an example where you can call "say" and it will emit a "hello" event every 1 second, and return "finished" at the end.

```javascript
class Hello {
  async say (request, ondata, kernel) {
    for(let i=0; i<10; i++) {
      // wait 1 second
      await new Promise(resolve => setTimeout(resolve, 1000));
      // emit "hello " + i event
      ondata({ raw: "hello" })
    }
    return "finished"
  }
}
module.exports = Hello
```

Try saving above file under `~/pinokio/api/hello/index.js`, and then create an example run script at `~/pinokio/api/hello/example.json`:

```json
{
  "run": [{
    "uri": "hello/index.js",
    "method": "say"
  }]
}
```

And when you run the `example.json` script, it will print "hello" to the terminal every 1 second, and after 10 seconds it will return "finished" and halt.

### kernel

Often, the RPC request won't be enough to carry out a task. For example you may need to access some low level methods or attributes.

You can use the `kernel` variable for this. Since the kernel object essentially gives you full access to the entire Pinokio operating system, I can't mention everything, but here are some notable modules worth looking at:

- `kernel`
  - [`sh()`](shell#shell): returns a new shell object
  - `api`: the `api` object (manages everything api related)
  - ...

## Example

### API with git URI

Let's imagine a simple script that contains one instruction:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    }
  }]
}
```

The first thing Pinokio does is figuring out which module and its method the `uri` resolves to, according to the [URI resolution convention](../fs/uri#http-path).

A git uri is made up of two components:

```
<remote git URI>/<relative path>
```

In the example above,

1. The `https://github.com/cocktailpeanut/llama.git` part is the `<remote git URI>`
2. The `index.js` part is the `<relative path>`

The actual algorithm:

1. **Begin URI parsing:** Pinokio sees the uri `https://github.com/cocktailpeanut/llama.git/index.js`
2. **Git uri extraction:** the git repository uri is extracted from the full uri: `https://github.com/cocktailpeanut/llama.git`
3. **Git config match:** Pinokio checks if there is any top level folder under `~/pinokio/api` whose `.git/config` includes the matching remote URL `https://github.com/cocktailpeanut/llama.git` (This would imply that the folder has been downloaded from a remote git repository available at the URL)
4. **Endpoint resolution:** If there's a match (let's say it finds one at `~/pinokio/api/llama`), the resolution is complete, and the request is routed to the module inside the matched local folder (`~/pinokio/api/llama`).
5. **Route resolution:** Now that the endpoint has been resolved, Pinokio looks at the `<relative path>` part of the full URI. In this case it's `index.js`. Pinokio takes the resolved endpoint path from the previous step (`~/pinokio/api/llama`) and resolves the rest of the file path `index.js`, and ends up with the full local path `~/pinokio/api/llama/index.js`.
6. **Method resolution:** Pinokio then looks at the JavaScript class file `~/pinokio/api/llama/index.js` and finds the method `run`
7. **Method Execution:** Now that Pinokio knows which method inside which file needs to be executed, the only thing left is to actually execute the method by passing the `params` attribute. 

The `~/pinokio/api/llama/index.js` must follow the [API framework convention](../apps/api#api-framework), and may look something like this:

```javascript
class Llama {
  async run (request, ondata, kernel) {

    // do stuff with the request.params

  }
}
module.exports = Llama
```

The `request` parameter will contain:

```json
{
  uri: 'https://github.com/malfunctionize/llama.git/index.js',
  method: 'run',
  params: {
    message: {
      p: "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
      m: '../models/stable-vicuna/13b_q4_0.bin',
      n: 256
    }
  },
  dirname: '/Users/x/pinokio/api/llama',
  cwd: '/Users/x/pinokio/api/llama/example',
  root: 'https://github.com/malfunctionize/llama.git/example/stable-vicuna-13b-q4_0.json',
  current: 0,
  next: null
}
```

1. `uri`: the full endpoint URI from the **begin URI parsing** step.
2. `method`: the RPC method passed in.
3. `params`: the RPC params passed in.
4. `dirname`: the resolved local path from the **endpoint resolution** step. This is the path under which the resolved module exists
5. `cwd`: the current execution path. This is the folder that contains the script that is running currently. 
6. `root`: the full path for the script file that is currently running.
7. `current`: The current instruction index within the `run` array. In this case it's 0 since it's the first instruction in the `run` array.
8. `next`: The next instruction index to be executed after the current request ends. In this case it's `null` since there is only one item in the `run` array (the current instruction), and `null` means the program will halt after this step.

### API with relative path

Now let's imagie the same script, but with relative path as its URI, instead of the remote git URI.

```json
{
  "run": [{
    "uri": "llama/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    }
  }]
}
```

Note that the `uri` is a relative path, which means it will be resolved to `~/pinokio/api/llama/index.js` according to the [URI resolution convention](../fs/uri#relative-path).

In this case there is no need for git URI resolution, since Pinokio simply needs to reach into the file that exists at the path `~/pinokio/api/llama/index.js`.

The rest of the resolution and execution logic is the same as the previous section.


# configure

# Configuring Apps

## Service mode apps

The "random" example was a very simple one, it was just a stateless function that is triggered every time you call it.

But there are so many other things you may want to do, that require a certain service running at all times.

For example imagine installing and running a StableDiffusion server. If we restarted StableDiffusion every time we made a request, it would be very slow. Instead, it's much more efficient to have a single StableDiffusion service running at all times, and have the service respond to the requests as they come in.

Some example use cases:

1. AI server
2. Database server
3. Websocket server

To accomplish this we need two things:

1. An easy way to allow people to install and launch the service
2. An automated relaunch whenever Pinokio restarts (otherwise you will have to go through all these service modules and manually restart every tiem you restart Pinokio)

## Installer

In essence, an "installation" is nothing more than running some shell commands.

You can achieve this using the built-in `sh` (shell) API. Here's an example for installing Automatic1111 (a StableDiffusion client) on a Mac:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "brew install cmake protobuf rust python@3.10 git wget",
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui automatic1111"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "sh webui.sh -f --api",
      "path": "automatic1111"
    }
  }]
}
```

1. Runs `brew install` to install dependencies
2. Runs `git clone` to download the automatic1111 repository
3. Runs `sh webui.sh -f --api` to start the installer

## Dynamic Installer

The problem with above script is that it only works on Mac.

For windows, or for linux, we need a different set of shell commands.

Fortunately we have multiple solutions for dynamically generating commands:

1. Use the [os](../processor/decode#os) variable to determine the OS inside templates.
2. Or, instead of using JSON, we write a JavaScript file that exports JSON dynamically!






# create

# Creating an API

Sometimes you may want to go further than just using the built-in core APIs, and write your OWN code that does something, and call THAT module using your own JSON-RPC syntax.


## Create an API folder

The entire Pinokio file system is stored under `~/pinokio`, and custom APIs are stored under `~/pinokio/api`.

So when building APIs locally, you just need to create a folder under `~/pinokio/api`.

Let's say we wanted to create a Pinokio script API for taking an array and returning a random item from the array. We will call this API endpoint `utils`, and the method name `random`.

For example:

```json
{
  "uri": "utils/index.js",
  "method": "random",
  "params": {
    "items": ["apple", "banana", "orange", "grape", "kiwi"];
  }
}
```

Let's get started by creating an API folder

```
cd ~/pinokio/api
mkdir utils
```

## Create an API class and a method

Now, go into the `utils` folder and create a JavaScript file named `index.js` at `~/pinokio/api/utils/index.js`.

> NOTE:
>
> We must use the exact file name `index.js` since this is how node.js resolves modules automatically.

Here is an example of what `index.js` may look like:

```javascript
class Utils {
  async random(request, ondata, kernel) {

  // Generate a random index within the range of the array length
  let randomIndex = Math.floor(Math.random() * items.length);

  // Access the item at the random index
  let randomItem = items[randomIndex];

  // Return the random item
  return randomItem
}
module.exports = Utils
```

Let's make sure that the API endpoint was created. All you need to do is go back to the Pinokio app and you will see the API show up on the home page. The home page automatically displays all folders under `~/pinokio/api`.



# form

# Autogenerating forms (advanced)

## What is a form?

Everything in Pinokio is JSON.

You can configure everything by simply opening the JSON files, updating, and saving:

![json.png](json.png)

But sometimes you may want to provide an easy-to-use UI for end users, so they can play with data easily **without having to directly tweak the JSON files**. Here's an example:

![form.png](form.png)

## How to generate a form

Pinokio provides an easy way to automatically generate forms like this for any JSON file. You can achieve this using the built-in form builder engine. Here's how it works:

1. Pick a JSON you want to generate a form for.
2. Create a JSON schema for the JSON.
3. Save the schema with a filename expected by Pinokio (Just add a `_` prefix to the original filename)
4. Now when you open the original JSON file, it will display the form view instead of the raw JSON.

For example, we havea `tumblr.json` file that we want to turn into a form:

![json.png](json.png)

We can do this by simply creating a file named `_tumblr.json` (note the `_` prefix) in the same folder and saving the JSON schema for the `tumblr.json` file:

![schema.png](schema.png)

Now when we visit the `tumblr.json` file, instead of the raw JSON view, we get the form view:

![form.png](form.png)

You can click the **View Source** button to switch to the JSON view.

## Getting a JSON schema

![schemagen.png](schemagen.png)

You can easily create a JSON schema from any JSON.

For example you can just use web apps like https://transform.tools/json-to-json-schema to enter any JSON and it will automatically generate a basic schema for you.

You can customize further on top of the basic schema if you want.

## Examples

### Case Study: Data Forms

Let's say we have an array stored at `animals.json`:

```json
[
  "Aardvark",
  "Ant",
  "Antelope"
]
```

And we want people to be able to edit this list WITHOUT touching the raw JSON, but through a form.

Just create a JSON schema file for `animals.json`, named `_animals.json`, in the same folder:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "animals",
  "type": "array",
  "items": {
    "type": "string",
    "title": "animal"
  }
}
```

Now when you open the `animals.json`, it will display the form view by default.

### Case Study: Config Forms

Another useful case is when you need to configure some engines, such as API clients.

Instead of making users manually edit JSON, you can auto-generate a form to set all the configuration fields.

Let's say we have built a tumblr API client script, and it requires the `tumblr.json` to be filled out before using:

```json
{
  "name": "",
  "config": {
    "consumer_key": "",
    "consumer_secret": "",
    "token": "",
    "token_secret": ""
  }
}
```

We can create a JSON schema file for `tumblr.json`, which will look like this:


```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "tumblr",
  "type": "object",
  "properties": {
    "required": [
      "name", "config"
    ],
    "name": {
      "type": "string",
      "title": "tumblr name"
    },
    "config": {
      "type": "object",
      "properties": {
        "required": [
          "consumer_key",
          "consumer_secret",
          "token",
          "token_secret"
        ],
        "consumer_key": {
          "type": "string"
        },
        "consumer_secret": {
          "type": "string"
        },
        "token": {
          "type": "string"
        },
        "token_secret": {
          "type": "string"
        }
      }
    }
  }
}
```

And now when the users open `tumblr.json`, they will get the form view, which is much easier to work with.



# overview

# Apps

Pinokio was designed to be extensible, which means you can build and publish your own APIs or your own apps.

![apps.gif](apps.gif)


All you need to do is: Write a JavaScript function that follows the Pinokio JSON-RPC protocol.

With Pinokio you can run:

1. Node modules
2. Python scripts
3. C programs
4. Any program you want

Basically there is no limit to what you can build.



# publish

# Publishing the API

Now that we know the API is working correctly, we want to share it with the world, so anyone can download and use our APIs.

There are a couple of things to note:

1. **Include an Example:** Package an example along with the API if possible. It's nice to be able to install an API and immediately try it out. You can set up a separate example repository, or include it in the same API folder.
2. **Switch examples to use the HTTP URI:** We've been using the relative path as the URI. But when publishing, we need to change the examples to use the public HTTP paths as URIs. For example, if I'm going to publish my `utils` API to `https://github.com/cocktailpeanut/utils.git`, I may want to go back and change all the examples to use the `"uri": "https://github.com/cocktailpeanut/utils.git/index.js"` instead of `utils/index.js` (Remember, people may download the repository to whichever folder name THEY want, so the relative path approach won't work anymore when you publish.)
3. **Publish to GitHub:** Publish to GitHub. You can publish to other git hosting services as well, but GitHub recommended for now [for discoverability](#list-on-pinokio).
4. **List:** When publishing to GitHub, tag your repository with `pinokio`, and it will automatically show up inside the Discover page in the Pinokio app.


## Include a README

Just like how GitHub automatically renders README.md files for any git repository, Pinokio also renders the `README.md` files. All you need to do is include the file in the root folder of your API repository.

a README documentation helps users easily use your API, so be as descriptive as possible.

## Include some examples

Also, it's great to include some example scripts, so the users who download your API can try out the API instantly without them having to write their own script to test.

For example,

1. just create an `example` folder and include the example scripts under the folder
2. link to the example scripts from `README.md`

Or if you want just a simple script, you can just create one `example.json` in the root folder. Choice is up to you.

## Examples must use HTTP URIs

One thing to remember when publishing APIs, is that once you publish, you shouldn't expect people to use the API by using the relative path you used while developing the API.

For example, you may have created a folder named `~/pinokio/api/utils`, but once you publish, another user may download it under `~/pinokio/api/utilities`, which means you can no longer assume that the `"uri"` will be `"utils"`.

From the moment you publish your repository, you can start using the public git URL, which means, if you've included some example scripts in your API repository, you should switch out all the relative paths to the public git URL. For example:

```json
{
  "run": [{
    "uri": "utils/index.js",
    "method": "random",
    "params": {
      "items": ["apple", "banana", "orange", "grape", "kiwi"];
    }
  }]
}
```

may become:


```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/utils.git/index.js",
    "method": "random",
    "params": {
      "items": ["apple", "banana", "orange", "grape", "kiwi"];
    }
  }]
}
```

> NOTE
> 
> The public git url MUST end with `.git`. This is the standardized way to reference git repositories.


## Publish to GitHub

Finally we're ready to publish.

There's nothing special here, just publish the repository to GitHub just like you publish any repository.

## List on Pinokio

![discover.png](discover.png)

Pinokio has a "discover" page which displays all the public Pinokio APIs published on GitHub.

To list your published API on the Pinokio discover page, just tag your repository with "pinokio", and it should immediately show up on the discover page:

![tagging.gif](tagging.gif)



# rpc

# RPC API

You can mix and match the core APIs (The kernel APIs) to build a sophisticated API or an app (script).

To make anything runnable, you simply need to create a JSON file with a "run" array.

Let's say you want to fetch some shell script from a URL and write it to a file, and then run it. Simply create a folder at `~/pinokio/api/test`, and create a pinokio script named `index.json`:


```json
{
  "run": [{
    "method": "net",
    "params": {
      "url": "https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh",
      "method": "get",
      "responseType": "text"
    }
  }, {
    "method": "fs.write", 
    "params": {
      "text": "{{input}}",
      "path": "install.sh"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "bash install.sh"
    }
  }]
}
```

And this is all you need to do! Just go to the `test` folder in Pinokio app and press "run", and it will execute these commands in order.



# shell

# Pinokio Shell Interface

At the core of Pinokio engine is its **JSON-RPC to Shell Interface**. Its features include:

1. Accept a JSON-RPC formatted request
2. Run ANY command
3. An ability to emit task progress in realtime
4. An interface to parse the terminal result and return a result

This engine powers the [sh](#shell-execution) API, you can also use it when building your own API/apps.

## Shell RPC

As discussed in the [Shell API](#shell-execution) section, You can already use the `sh` method to run shell commands. For example:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/cocktailpeanut/pinokio"
    }
  }]
}
```

While this works perfectly fine for most use cases, sometimes you may want a more low level access to the Pinokio shell interface.

To achieve this, we can directly use the Pinokio shell programattically, instead of using the `sh` API.


## Shell

To put simply, the `sh` API is a JSON-RPC API(remote procedure call) interface to calling the low level shell interface.

But we can directly use the low level shell interface when needed. Some use cases:

1. You need to build a custom app or api that uses the shell, as well as other JavaScript code.
2. You need to process the realtime stream and trigger custom events when certain conditions are met.


The Shell interface is a JavaScript module that gives you full access to the shell stream.

### Creating a shell session

1. The shell interface is accessible as an attribute under the [kernel parameter](api#kernel) when writing an API method.
2. You can acquire a fresh handle to a shell session using `kerhel.sh()`

```javascript
class MyAPI {
  async run(request, ondata, kernel) {

    // 1. get a fresh shell interface
    let sh = kernel.sh()

    // 2. do stuff with the shell
  }
}
module.exports = MyAPI
```

### Making a request to the shell session

Once you have the shell handle, you can make requests to it to run commands:

1. You can make requests to the shell using `sh.request({ message, path }, ondata)` (where `ondata()` is a callback function that streams data (string) in realtime.
2. The `sh.request()` method returns a promise that gets resolved when the command execution is over.
3. The `sh.request()` method does NOT return if you run a command that never returns (for example starting a server that keeps running)


```javascript
class MyAPI {
  async run(request, ondata, kernel) {

    // 1. get a fresh shell interface
    let sh = kernel.sh()

    // 2. make a request to the shell
    let result = await sh.request(request, (stream) => {
      
      // 3. do something with the realtime stream here...

    })

    // 4. do stuff with the terminal string `result`
    return result   // for example you can return `result` immediately, and the `run` method for your API will return `result` as the return value

  }
}
module.exports = MyAPI
```

For example, let's say we want to write an API that runs a python script `run.py` and returns the printed result as the return value.

But there's a twist. The python script prints a lot of things on the screen, and we may only want to extract certain pattern from the full text.

For example, we may want to only extract the part of the full text that's wrapped with `<pinokio></pinokio>`.

```javascript
class Pycaller {
  async run(request, ondata, kernel) {
    /*****************************************************************************************

      EXAMPLE: take a script name, run it, and return the printed result as the return value

      request := {
        method: "run",
        params: {
          script: "run.py"
        }
      }

    *****************************************************************************************/

    // 1. get a fresh shell interface
    let sh = kernel.sh()

    // 2. Compose shell request
    let shell_request = {
      message: `python ${request.params.script}`
    }

    // 3. make a request to the shell
    let result = await sh.request(shell_request, (stream) => {

      // 4. let's emit the incoming data stream as event => This will be automatically displayed in the Pinokio terminal in realtime
      ondata(stream)

    })

    // 5. When the command has finished, extract only the substring that matches `<pinokio>...</pinokio>` pattern and return this as the return value
    const pattern = /<pinokio>(.*?)<\/pinokio>/g;
    const matches = result.match(pattern);

    return matches

  }
}
module.exports = Pycaller
```

As you can see, in this case we are using the shell but also running some post processing tasks (extracting out the `<pinokio>...</pinokio>` patterns before returning), and in this case it's much simpler to write this JavaScript function and use the low level Shell interface instead of trying to do all of this using the `sh` JSON-RPC API.


### Processing the realtime stream

Briefly mentioned above, but often we may want to emit events during the execution in order to notify the client of the progress.

We can use the `ondata()` callback inside the callback function (the second argument in the call `sh.request(request, (stream) => { // do stuff with the stream })`.

```javascript
class MyAPI {
  async run(request, ondata, kernel) {

    // 1. get a fresh shell interface
    let sh = kernel.sh()

    // 2. make a request to the shell
    let started
    await sh.request(req, (stream) => {
      /******************************************************************************

        stream := {
          raw: <the raw text stream (including ANSI escape sequences)>,
          cleaned: <the cleaned version of the full terminal history>
        }

        1. raw: the realtime data stream
        2. cleaned: not a stream, but the full text view of the virtual terminal

      ******************************************************************************/


      // Option 1. We can pass all the raw terminal events to the client
      ondata(stream)

      // Option 2. We can process the `stream.cleaned` attribute to detect any string pattern
      let buffer = ""
      if (this.started) {
        // 1. At first, this.started is "undefined" so this part of the code is never run until this.started is set to true.
        // 2. This is because we may not be interested in the raw stream until we see some start markers.
        // 3. Once "this.started" is set to true, we can then start collecting the incoming data stream in to the buffer
        buffer += stream.raw
      } else {
        // 1. At first this.started is "undefined" so this part of the code will be executed for every incoming event.
        // 2. we keep testing for a pattern and wait until the cleaned terminal text matches some pattern, and set the "started" to true
        // 3. In this case, we are waiting for the "### Response" pattern to show up at least twice, and only when that happens we set this.started to true
        let test = /### Response.*### Response/gs.test(stream.cleaned)
        if (test) {
          this.started = true
        }
      }
    })

    // We finally return the "buffer" string as the response
    return buffer

  }
}
module.exports = MyAPI
```

### Killing a shell session

1. You can manually kill the `sh.request()` process by calling `sh.kill()`
2. When you call `sh.kill()`, the original promise returned by `sh.request()` is resolved.



```javascript
class MyAPI {
  async run(request, ondata, kernel) {

    // 1. get a fresh shell interface
    let sh = kernel.sh()

    // 2. make a request to the shell
    let started
    await sh.request(req, (stream) => {
      
      // 3. do something with the realtime stream := { raw, cleaned }

      // Example a. printing to the screen
      process.stdout.write(stream.raw)

      // Example b. emit websocket events to all connected sessions
      ondata(stream)

      // Example 3. wait until some pattern appears
      if (started) {
        // only triggered after the "started" is set to true
        // do something with the stream
      } else {
        // wait until the cleaned text matches some pattern, and set the "started" to true
        let test = /### Response.*### Response/gs.test(stream.cleaned)
        if (test) {
          started = true
        }
      }
    })

  }
}
module.exports = MyAPI
```



# test

# Testing the API

Now let's test this API to make sure it works.

Let's write a simple Pinokio run script and store it in the same folder as `example.json` (`~/pinokio/api/utils/example.json`):

```json
{
  "run": [{
    "uri": "utils/index.js",
    "method": "random",
    "params": {
      "items": ["apple", "banana", "orange", "grape", "kiwi"];
    }
  }, {
    "method": "fs.write",
    "params": {
      "text": "{{input}}",
      "path": "random.txt"
    }
  }]
}
```

Now go back to Pinokio app and you will see that the `example.json` file shows up in the explorer. Click, and you'll see the script runner page, with a "run" button.

Click the button and it will run:

1. Get a random item from the given array
2. Write the random item to `random.txt` in the same folder.

After running the script, inside the Pinokio app (or in your OS file explorer) check to see that the `random.txt` file has been created and it contains a random item from the array.

Try clicking the "run" button multiple times, and you will see that every time you press the button, the contents of the `random.txt` file changes.



# quickstart

# Quickstart

Let's try writing a custom API.

This example will simply take an array of numbers, and return the total.

We will call the API "sum"

![sum.gif](sum.gif)

## 1. Create a project

We need to first create a project. Create a folder under `~/pinokio/api`:

```
cd ~/pinokio/api
mkdir sum
```

## 2. Create a Pinokio script

Let's first create a script file.

Create a file named `run.json` under the `~/pinokio/api/sum` folder we just created:

```json
{
  "run": [{
    "uri": "./api.js",
    "method": "sum",
    "params": [1,2,3,4,5,6,7,8,9,10]
  }]
}
```


## 3. Create an API file

As we can see from the request object, this request will look for a file named `./api.js`:


```json
{
  "uri": "./api.js",
  "method": "sum",
  "params": [1,2,3,4,5,6,7,8,9,10]
}
```

So let's create a file named `api.js` in the same folder as the request script (`~/pinokio/api/sum`):


```javascript
// api.js
class API {
  async sum (req, ondata, kernel) {
    // add all the items in the req.params array and return the result
    let sum = 0
    for(let item of req.params) {
      sum += item
    }
    return sum
  }
}
module.exports = API
```

## 4. Run in Pinokio

And that's all there is to it!

1. Open Pinokio and you will see the `sum` folder you've just created.
2. Navigate into the folder and click the **run.json** file, and click "Run".
3. You will see that it correctly calculates the sum of all the numbers and returns 55.

![sum.gif](sum.gif)

The return value of the API is printed right below the terminal.

## 5. Displaying progress

In many cases, calling a shell command takes a while to finish and you may want to display the progress of the API call.

To emulate this, let's try to artificially slow down the API execution first, and go from there. We will add a 1 second delay inside the for loop:

```javascript
// api.js
class API {
  async sum (req, ondata, kernel) {
    // add all the items in the req.params array and return the result
    let sum = 0
    for(let item of req.params) {
      sum += item

      // [ADDED] 1 second delay
      await new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve()
        }, 1000)
      })

    }
    return sum
  }
}
module.exports = API
```

Now when you run the `run.json`, you will get the response (55) after 10 seconds.

As we mentioned above, in these cases we may want to display the progress so the users are aware of what's going on.

We can accomplish this with the `ondata()` callback passed in as the second parameter of the `sum()` method:


```javascript
// api.js
class API {
  async sum (req, ondata, kernel) {
    // add all the items in the req.params array and return the result
    let sum = 0
    for(let item of req.params) {
      sum += item

      await new Promise((resolve, reject) => {
        setTimeout(() => {
          resolve()
        }, 1000)
      })

      // [ADDED] Print progress
      ondata({
        raw: sum + "\r\n"
      })

    }
    return sum
  }
}
module.exports = API
```

This will stream the "raw" string to the terminal, and you will see that the current sum for every loop will be printed every 1 second:

![progress.gif](progress.gif)

## 6. Calling APIs

So far, we have created an API and included a companion script that calls the API.

It's important to remember that both the API and the script are part of the same repository. This is why we could use the realtive path as uri (`./api.js`) when calling the API:

```json
{
  "run": [{
    "uri": "./api.js",
    "method": "sum",
    "params": [1,2,3,4,5,6,7,8,9,10]
  }]
}
```

But in many cases, you may simply want to call an EXISTING API from your script.

To accomplish this, all you need to do is:

1. Install the API (assuming that the API has been published to a public git URI)
2. Call the API using the public git URI intead of realtive path.


```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/sum.git/api.js",
    "method": "sum",
    "params": [1,2,3,4,5,6,7,8,9,10]
  }]
}
```

## 7. Specifying dependencies

When running the script from the last section, we are assuming that the API published at `"https://github.com/cocktailpeanut/sum.git/api.js"` has been downloaded and exists locally.

Basically, to make sure that anyone who downloads your script can run your script, you need to let these people know that they need to have these APIs installed on their machines.

You can achieve this by specifying an attribute named `"dependencies"` in a file named `pinokio.js` in your script folder.

```javascript
module.exports = {
  dependencies: [ "https://github.com/cocktailpeanut/sum.git" ]
}
```

Then browse to the script folder, and you will see that Pinokio now suggests the "Prerequisites" based on the dependencies array.

![dependencies.png](dependencies.png)


## 8. Using 3rd party libraries and engines

Often you may want to import 3rd party libraries or carry out some sophisticated tasks before being able to use the API. For example:

1. Build an API using 3rd party NPM packages (such as `next.js`, `nodemailer`, `GraphicsMagick`, etc)
2. Start a server before running the API (such as database systems, servers, etc.)

Fortunately, pinokio has various building blocks to make these things more user friendly.

### Installers

For example, let's say you are building a Pinokio API that uses the `nodemailer` package to send emails. You may want to create an install script named **install.json**:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "npm install nodemailer"
    }
  }]
}
```

Then, to make it more visible to the end users you can:

1. either include it in the README.md as a link
2. or add a menu bar button with pinokio.js: [learn more](/tutorial/menu)

### Start scripts

Often you may want your API to automatically start a server or a connection when Pinokio starts.

For example if your API involves a database system, you will probably want to make sure that your DB automatically starts up when Pinokio starts, so the endpoint will be available when you make API requests immediately after.

In these cases, you can use the [self driving scripts](/tutorial/autostart) to automatically launch whatever services you need, automatically.


# reference

# Reference

First of all, a Pinokio API is nothing more than **a mapping from JSON-RPC to a JavaScript function call.**

## Rules

To build your own API, you need to follow the convention expected by the Pinokio API framework.

All Pinokio functions must take the following form:

1. Every API should be stored under its own uniquely named folder under `~/pinokio/api`.
2. The API file must be a JavaScript class with `index.js` as its filename.
3. The JavaScript class must have one or more methods. The method names are important since they will be used in JSON-RPC calls.
4. The methods must follow a specific function signature convention expected by the Pinokio API framework

## API Class

Let's say we want to create an API that takes a JSON-RPC request like this:

```json
{
  "uri": "./echo.js",
  "method": "run",
  "params": {
    "text": "hello world"
  }
}
```

and returns the same value `params.text` (`"hello world"`).

To accomplish this, we just need to write a JavaScript class and a method that looks something like this:

```javascript
class Echo {
  async run (request, ondata, kernel) {
    return request.params.text 
  }
}
module.exports = Echo
```

### class name

The name of the class (`Echo` in this example) here is not important and you can name it whatever you want.

### file name

The file name however, is important. In this case, since the uri is set to `./echo.js`, we need to place the `echo.js` file in the same folder as the Pinokio script JSON file.


## API Method

Each method must follow the protocol (must have a specific function signature):

```javascript
async (request, ondata, kernel) {
  // 1. do something with the request (the JSON-RPC payload)
  // 2. use ondata() to send realtime updates during execution 
  // 3. use kernel to access some kernel level attributes and methods
  // 4. finally, return a value (in case this API has a return value)
}
```

Let's walk through each parameter one by one:

1. request
2. ondata
3. kernel

### request

The `request` object is used to utilize the JSON-RPC request object as well as some additional information.

- `request`: The JSON-RPC request object, along with some additional metadata attached by the Pinokio processor
  - `uri`: The request destination URI
  - `method`: The request method
  - `params`: The request parameter. This is the attribute that's used most frequently to implement APIs
  - `dirname`: The absolute path of the folder that contains the API file being called (For example, `~/pinokio/api/utils`)
  - `cwd`: The absolute path of the folder from which the script is being called. The difference from `dirname` is that the `cwd` is the folder path of the run script that's currently calling this API, whereas the `dirname` is the folder path of the API file being called. Similar to the difference between [process.cwd() and __dirname in node.js](https://www.tutorialspoint.com/difference-between-process-cwd-and-dirname-in-nodejs)
  - `parent`: The parent script file object. Every API call in a single script shares the same `parent` object.
    - `uri`: The uri of the parent script
    - `path`: The absolute file path of the parent script
    - `body`: The actual script body object.
  - `current`: The current instruction index within the `run` array.
  - `next`: The next instruction index within the `run` array. `null` if the current instruction is the last step in the `run` array.


### ondata

The `ondata()` callback function is used to emit events while the API is running.

Often (especially when using AI engines), a single API call may take a while to finish, and it is useful to be able to notify the realtime progress update to the client. 

You can call the `ondata()` callback to trigger these events.

```javascript
ondata(data)
```

- `data`: the raw data stream (string). may includes the following attributes:
  - `raw`: The raw string (can include ANSI characters and escape sequences, and translates 1:1 to a terminal display). Emit this attribute if you need to display escape sequences in the terminal.
  - `state`: The full state representation of the current state. While `raw` represents individual events, the `state` is a single full string that represents the current state.

Here's an example where you can call "say" and it will emit a "hello" event every 1 second, and return "finished" at the end.

```javascript
class Hello {
  async say (request, ondata, kernel) {
    for(let i=0; i<10; i++) {
      // wait 1 second
      await new Promise(resolve => setTimeout(resolve, 1000));
      // emit "hello " + i event
      ondata({ raw: "hello" })
    }
    return "finished"
  }
}
module.exports = Hello
```

Try saving above file under `~/pinokio/api/hello/index.js`, and then create an example run script at `~/pinokio/api/hello/example.json`:

```json
{
  "run": [{
    "uri": "hello/index.js",
    "method": "say"
  }]
}
```

And when you run the `example.json` script, it will print "hello" to the terminal every 1 second, and after 10 seconds it will return "finished" and halt.

### kernel

Often, the RPC request won't be enough to carry out a task. For example you may need to access some low level methods or attributes.

You can use the `kernel` variable for this. Since the kernel object essentially gives you full access to the entire Pinokio operating system, I can't mention everything, but here are some notable modules worth looking at:

- `kernel`
  - shell: You can use the low level Shell API with [kernel.shell](/custom/shell)

## Example

### API with git URI

Let's imagine a simple script that contains one instruction:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    }
  }]
}
```

The first thing Pinokio does is figuring out which module and its method the `uri` resolves to, according to the [URI resolution convention](../fs/uri#http-path).

A git uri is made up of two components:

```
<remote git URI>/<relative path>
```

In the example above,

1. The `https://github.com/cocktailpeanut/llama.git` part is the `<remote git URI>`
2. The `index.js` part is the `<relative path>`

The actual algorithm:

1. **Begin URI parsing:** Pinokio sees the uri `https://github.com/cocktailpeanut/llama.git/index.js`
2. **Git uri extraction:** the git repository uri is extracted from the full uri: `https://github.com/cocktailpeanut/llama.git`
3. **Git config match:** Pinokio checks if there is any top level folder under `~/pinokio/api` whose `.git/config` includes the matching remote URL `https://github.com/cocktailpeanut/llama.git` (This would imply that the folder has been downloaded from a remote git repository available at the URL)
4. **Endpoint resolution:** If there's a match (let's say it finds one at `~/pinokio/api/llama`), the resolution is complete, and the request is routed to the module inside the matched local folder (`~/pinokio/api/llama`).
5. **Route resolution:** Now that the endpoint has been resolved, Pinokio looks at the `<relative path>` part of the full URI. In this case it's `index.js`. Pinokio takes the resolved endpoint path from the previous step (`~/pinokio/api/llama`) and resolves the rest of the file path `index.js`, and ends up with the full local path `~/pinokio/api/llama/index.js`.
6. **Method resolution:** Pinokio then looks at the JavaScript class file `~/pinokio/api/llama/index.js` and finds the method `run`
7. **Method Execution:** Now that Pinokio knows which method inside which file needs to be executed, the only thing left is to actually execute the method by passing the `params` attribute. 

The `~/pinokio/api/llama/index.js` must follow the [API framework convention](../apps/api#api-framework), and may look something like this:

```javascript
class Llama {
  async run (request, ondata, kernel) {

    // do stuff with the request.params

  }
}
module.exports = Llama
```

The `request` parameter will contain:

```json
{
  uri: 'https://github.com/malfunctionize/llama.git/index.js',
  method: 'run',
  params: {
    message: {
      p: "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
      m: '../models/stable-vicuna/13b_q4_0.bin',
      n: 256
    }
  },
  dirname: '/Users/x/pinokio/api/llama',
  cwd: '/Users/x/pinokio/api/llama/example',
  root: 'https://github.com/malfunctionize/llama.git/example/stable-vicuna-13b-q4_0.json',
  current: 0,
  next: null
}
```

1. `uri`: the full endpoint URI from the **begin URI parsing** step.
2. `method`: the RPC method passed in.
3. `params`: the RPC params passed in.
4. `dirname`: the resolved local path from the **endpoint resolution** step. This is the path under which the resolved module exists
5. `cwd`: the current execution path. This is the folder that contains the script that is running currently. 
6. `root`: the full path for the script file that is currently running.
7. `current`: The current instruction index within the `run` array. In this case it's 0 since it's the first instruction in the `run` array.
8. `next`: The next instruction index to be executed after the current request ends. In this case it's `null` since there is only one item in the `run` array (the current instruction), and `null` means the program will halt after this step.


### API with relative path

Now let's imagie the same script, but with relative path as its URI, instead of the remote git URI.

```json
{
  "run": [{
    "uri": "./index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    }
  }]
}
```

Note that the `uri` is a relative path, so it will look for the `index.js` file in the same folder as the script file itself.



# shell

# JavaScript Shell API

One of Pinokio's most powerful features is the [Shell JSON-RPC API](/api/shell), which lets you interact with the shell with nothing but JSON.

While the JSON-RPC API is already powerful and you should be able to achieve most of what you want using the JSON-RPC API, sometimes you may want more low level access to the shell.

Basically, instead of including the shell execution code in your JSON script (the "frontend"), you may want to write the shell manipulation logic in your custom API code (the "backend").


## How to access

The shell API is available at `kernel.shell` when writing your own custom API method:

```javascript
class CustomAPI {
  async customMethod(req, ondata, kernel) {
    // Access the JavaScript shell API with "kernel.shell"
    await kernel.shell.run({
      message: "npm init"
    })
  }
}
```

## Modes

There are two ways to use the shell:

1. **Request/Response mode:** Use it like a web server. Making a request creates a shell, runs the command, and returns the response. The created shell is destroyed at the end of the request.
2. **Persistent mode:** Use it like a socket server, by creating a persistent connection and sending messages. The shell session is not destroyed until it encounters an event you specify.

## 1. Request/Response mode

### shell.run

```javascript
let response = await kernel.shell.run(params, options, ondata)
```

#### parameters

- **params:** shell request params
- **options:** optional
  - **group:** group id. used to group shell sessions, so they can be stopped later by group id.
  - **cwd:** base path. if not specified, the cwd is set as ~/pinokio

#### return value

- **response:** The full terminal text

## 2. Persistent mode

### shell.start

```javascript
let id = await kernel.shell.start(params, options)
```

#### parameters

- **params:** shell request params
- **options:** optional
  - **group:** group id. used to group shell sessions, so they can be stopped later by group id.
  - **cwd:** base path. if not specified, the cwd is set as ~/pinokio

#### return value

- **id:** The created shell id

### shell.enter

```javascript
let response = await kernel.shell.enter(params, ondata)
```

#### parameters

- **params:** shell request params
- **ondata:** realtime callback that gets called for every shell event. Triggers the following event object:
  - **id:** The shell ID
  - **raw:** Raw event string
  - **state** The full terminal text when the event was triggered

#### return value

- **response:** The full terminal text

### shell.write

```javascript
let response = await kernel.shell.write(params, ondata)
```

#### parameters

- **params:** shell request params
- **ondata:** realtime callback that gets called for every shell event. Triggers the following event object:
  - **id:** The shell ID
  - **raw:** Raw event string
  - **state** The full terminal text when the event was triggered

#### return value

- **response:** The full terminal text

### shell.stop

```javascript
await kernel.shell.stop(query)
```

- **query**
  - **id:** stop a shell session by ID
  - **group:** stop all shell sessions that belong to the group




# what

# What is an API?

## Local first API

In Pinokio, APIs are local JavaScript classes that behave like remote servers.

It's easy to understand when we compare it to traditional APIs.

## Traditional API vs. Pinokio API

### Traditional API

Here's an example "traditional" API request:

```
POST /test HTTP/1.1
Host: foo.example
Content-Type: application/x-www-form-urlencoded
Content-Length: 27

field1=value1&field2=value2
```

Basically it's making a:

1. **POST** request
2. to the route **/test**
3. at a remote server **foo.example**
4. by passing the key value pairs **field1=value1&field2=value2**

### Pinokio API

With Pinokio, all APIs exist locally.

Instead of making a request to a remote server, the API requests go to locally installed JavaScript modules.

Here's an example Pinokio request:

```json
{
  "uri": "https://github.com/cocktailpeanut/sum.git/api.js",
  "method": "sum",
  "params": [1,2,3,4,5]
}
```

Here's how it works:

1. First download the JavaScript module at `https://github.com/cocktailpeanut/sum.git` (**NOTE: the URI is used to DOWNLOAD the entire repository, not to make a reuqest to it**)
2. Resolve the endpoint by importing the JavaScript module at `api.js`
3. Look up the exported `sum()` inside the `api.js` file
4. Pass in the `params` to the resolved `sum()` method.
5. The `sum()` method does its job and returns a response.

Basically, everything happens locally but it resembles a network request.

## Building a custom API

Therefore, building a custom API simply means writing a JavaScript module that follows a certain convention (will be explained in the following sections).

All you need to do is write a single JavaScript module while following the Pinokio JavaScript API convention, and you should be able to immediately start calling these API "backends" using JSON scripts.


# applemac

# Pinokio for Mac M1/M2 chip

<br>

## Step 1. Download

<a href="https://github.com/pinokiocomputer/pinokio/releases/download/0.0.56/Pinokio-0.0.56-arm64.dmg" class='btn'>Click to Download Pinokio for M1 & M2 Macs</a>

<br>

## Step 2. Install

![macinstall.gif](macinstall.gif)

1. Run the downloaded DMG installer file
2. Drag the "Pinokio" app to the Applications folder
3. Run the "patch.command"
4. Open the Pinokio app in the applications folder


# index

# Download Pinokio

- [Windows](windows)
- [M1 & M2 Mac](applemac)
- [Intel Mac](intelmac)
- [Linux](linux)


# intelmac

# Pinokio for Mac Intel chip

<br>

## Step 1. Download

<a href="https://github.com/pinokiocomputer/pinokio/releases/download/0.0.56/Pinokio-0.0.56.dmg" class='btn'>Click to Download Pinokio for Intel Macs</a>

<br>

## Step 2. Install

![macinstall.gif](macinstall.gif)

1. Run the downloaded DMG installer file
2. Drag the "Pinokio" app to the Applications folder
3. Run the "patch.command"
4. Open the Pinokio app in the applications folder


# linux

# Pinokio for Linux

<br>

For linux, download and install directly from the latest release on Github

<a href="https://github.com/pinokiocomputer/pinokio/releases" class='btn'>Download from GitHub</a>


# windows

# Pinokio for Windows

<br>

## Step 1. Download

<a href="https://github.com/pinokiocomputer/pinokio/releases/download/0.0.56/Pinokio-0.0.56-win32.zip" class='btn'>Click to Download Pinokio for Windows</a>

<br>

## Step 2. Unzip

Unzip the downloaded file and you will see a **.exe** installer file.

<br>

## Step 3. Install

Run the installer file and you will be presented with the following Windows warning:


![installwin.gif](installwin.gif)

This message shows up because the app was downloaded from the Web, and this is what Windows does for apps downloaded from the web.

To bypass this,

1. Click "More Info"
2. Then click "Run anyway"


# overview

# File System

![library.png](library.png)

## Everything is a file

Everything on Pinokio exists as a file.

### Flat File

The Pinokio world is made up of files. Everything can be expressed with files.

More specifically, Pinokio lets you express everything using flat **JSON files**:

1. **Data:** Data stored as JSON.
2. **Code:** Code written in JSON ([JSON-RPC](https://www.jsonrpc.org/specification)).
3. **API:** Automatically constructed API endpoints based on file path convention.
4. **UI:** UI expressed in JSON (Autogenerated forms based on [JSON Schema](https://json-schema.org/)).
5. **Publishing:** Because everything can be replicated deterministically through files, it becomes trivial to publish and share the AIs created using Pinokio.
    - Publish to Git to version control and allow others to easily clone or fork
    - Publish to IPFS or BitTorrent for decentralized AI publishing.
    - etc.

### Unix Philosophy

The benefit of the ["Everything is a file"](https://en.wikipedia.org/wiki/Everything_is_a_file) approach is explained here:

> Everything is a file is an idea that Unix, and its derivatives, handle input/output to and from resources such as documents, hard-drives, modems, keyboards, printers and even some inter-process and network communications as simple streams of bytes exposed through the filesystem name space.
> ...
> The advantage of this approach is that the same set of tools, utilities and APIs can be used on a wide range of resources and a number of file types. When a file is opened, a file descriptor is created, using the file path as an addressing system. The file descriptor is then a byte stream I/O interface on which file operations are performed
>
> https://en.wikipedia.org/wiki/Everything_is_a_file

Pinokio follows the same philosophy and enjoys the same benefits.

### Benefits

1. **Shareable:** Because all you need is JSON, it is not only easy to build complex workflows, but also easy to share the workflows, simply by publishing the files (to git, etc).
2. **Self-contained:** Because everything (not just data, but also code) is stored and executed as a file, Pinokio does not have any dependency on some 3rd party system. You can build and publish a completely self contained archive of workflows and applications as a single file or a folder.
4. **Natively Modular:** Everything existing as a file makes it easy to automatically separate a monolithic application (expressed in a single JSON file) out into multiple files (also expressed in JSON files)
5. **Dynamic data powered by templates:** Since everything is stored as a flat file, we can implement dynamic data simply by incorporating template expressions in those files (`{{ }}`), and they are all automatically decoded at runtime.
4. **Simplified Application Development:** No complex configuration is needed for building applications. Simply write some JSON or JavaScript files and drop them under the project folder, and the app constructs itself.
5. **Cross platform:** The flat file format makes it trivial to run the same logic on multiple different platforms.
6. **Easily extensible:** The native JSON file format makes it easy to extend APIs and applications simply by modifying the JSON attributes.

### JSON Protocol

It is important to note that Pinokio uses JSON not just for storing data and code, but also as the native protocol.

In addition to everything from data to code being stored as JSON, Pinokio can use JSON to integrate and and comunicate with ANY external processes and remote APIs. Some examples:


1. **Run any python script:** To communicate with a python process, simply write a JSON file from the python process, or print JSON to stdout from the python script, and process the terminal stream using the [Pinokio Shell Interface](../apps/shell)
2. **Call any external process:** Going one step further, it's not just python you can run. If you can run something manually, Pinokio can automate it with a simple [sh RPC](../api/shell), or utilize the [Pinokio Shell Interface](../apps/shell) for more low level access and stream processing.
3. **Call external servers:** JSON is the most popular data transmission format for most APIs. You can communicate with any external API using the [net API](../api/networking) and seamlessly incorporate it into applications.


## Home directory

Pinokio stores everything inside the `pinokio` folder under the user home directory (`~/pinokio`).

Example:

- **windows:** `C:\Users\<username>\pinokio`
- **linux:** `/home/<username>/pinokio`
- **mac:** `/Users/<username>/pinokio`

## Folder structure

The top level directories look like the following:

```
~/
  /pinokio
    /api    # (~/pinokio/api) stores the user installed files
    /bin    # (~/pinokio/bin) stores binary files, such as cmake, git, python, etc.
```

### bin

The `bin` folder stores all the binaries commonly used by AI engines. Currently includes:

- **python** (and `pip`)
- **node.js** (and `npm`)
- **git** (only on windows for now, since mac and linux mostly ships with git)
- **cmake** used for building C projects
- more coming soon (please request if you need something)

### api

The `api` folder is where the user downloaded repositories are stored. An API folder can contain either of the following:

1. **downloaded from git:** repositories you downloaded from git.
2. **locally created:** you can manually create folders and work from there.



# structure

# Structure

```
~
  /pinokio
    /api    # stores the user installed files
    /bin    # stores binary files, such as cmake, git, python, etc.
```

## bin

The `bin` folder stores all the binaries commonly used by AI engines. Currently includes:

- **python** (and `pip`)
- **node.js**
- **git** (only on windows for now, since mac and linux mostly ships with git)
- **cmake** used for building C projects
- more coming soon (please request if you need something)

## api

The `api` folder is where the user downloaded repositories are stored. An API folder can contain either of the following:

1. **downloaded from git:** repositories you downloaded from git.
2. **locally created:** you can manually create folders and work from there.

A Pinokio API is a completely local.


# uri

# URI

## What is a Pinokio URI?

### Requirements

Normally when we talk about APIs, we think of **remote web servers that can be configured to expose one or more public routes**, to which you can make requests.

However, Pinokio API was designed with a unique set of assumptions:

1. **Local First:** Unlike traditional APIs that assume remote execution, Pinokio assumes the primary use case is interacting with the local machine to carry out tasks. This "local first" assumption is important for running AI tasks with privacy and without censorship.
2. **Zero Configuration:** APIs should require zero configuration, and should "just work" out of the box.
4. **Globally unique resource identifiers for locally hosted APIs:** This sounds like an oxymoron, but it is a unique challenge for autonomous AI engines, because while we assume that the actual task execution will happen locally, there needs to be some way to globally address these locally hosted endpoints. An example solution adopted by Pinokio is to use [public git URIs for calling APIs](#http-path).

### Implementation

1. **JSON RPC:** All API requests are [JSON-RPC](https://www.jsonrpc.org/specification) calls (instead of [REST](https://en.wikipedia.org/wiki/Representational_state_transfer) based)
2. **Automatic 1:1 mapping to local file paths:** Unlike traditional APIs where you can only make requests to manually configured routes, Pinokio automatically creates an endpoint for EVERY file path under the Pinokio file system.
3. **Convention over Configuration:** To automatically map JSON-RPC calls to local file paths, the Pinokio URI framework has a convention you can follow instead of manually specifying exposed routes.


Basically, Pinokio API URIs are unique resource identifiers that automatically map to locally installed folders via HTTP.

## Instant URI

### Convention over Configuration

Similar to how [next.js automatically sets up routes based on convention](https://nextjs.org/docs/pages/building-your-application/routing), Pinokio lets you simply place your workspace folders under the `~/pinokio/api` top level folder, and the files inside your workspace folders will be instantly made available for API reqeusts, each available at URIs based on the file and folder paths.

## URI Types

When making an API request to a Pinokio engine, you can use any of the following 3 URI schemes:

2. Relative path
3. HTTP path

Note that all of these URI schemes resolve to a local file path (even when using the HTTP path option).


### Relative Path

A URI can be a file path. Let's imagine an example project:

```
~/pinokio
  /test
    run.json
    /bin
      install.json
```

Where the `run.json` script looks like this:

```json
{
  "run": [{
    "uri": "./bin/install.json",
    "method": "run",
    "params": {
      ... 
    }
  }]
}
```

Note that the relative path `./bin/install.json` will be resolved against the path of the calling script (`run.json`).


### HTTP Path

An HTTP path exists ONLY for the folders you downloaded from a remote git repository.

#### Spec

The HTTP path is equivalent to the remote git URI, followed by the relative path within the git repository. It takes the following format:

```
<remote git URI>/<relative path>
```

For example, to reference a file at `index.js` inside the https://github.com/cocktailpeanut/llama.git git repository, the HTTP path would look like:

https://github.com/cocktailpeanut/llama.git/index.js


#### How it works

Although the URL looks like a typical HTTP url, it's important to note that the you are not actually making an API request to https://github.com/cocktailpeanut/llama.git/index.js

1. The URI is just a unique identifier used to identify the endpoint and the method to call
2. The `remote git URI` and `relative path` combination is used to uniquely identify where the API files exist on your machine.

#### Where the files are stored

When you download an API from a git repository, Pinokio stores them under the **hex version of the remote git URI**.

For example, if the remote git URI you downloaded were https://github.com/cocktailpeanut/llama.git - Pinokio automatically creates a folder named `0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974` (This is the hex version of the URI) and downloads the remote git repository to that folder.

```
~
  /pinokio
    /api
      /0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974
```

Note that Pinokio automatically generates these folder names when you download APIs from git repositories, but when you're building your own app or api locally, you can name the folders whatever you want:

![folders.png](folders.png)

In above example, the first 4 folders with hex names are the downloaded APIs, whereas the next 2 (**helloworld** and **test**) are locally created folders.


#### Rules

Some rules:

1. The `<remote git URI>` must end with `.git` (This is the standard way to reference git repositories)
2. The URL info is derived from the `.git/config` file within the downloaded repository.

#### Example

This section will explain how the URI to local path resolution is actually carried out.

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "p": "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "n": 256
      }
    }
  }]
}
```

In above example,

1. The `https://github.com/cocktailpeanut/llama.git` part is the `<remote git URI>`
2. The `index.js` part is the `<relative path>`

Resolution algorithm:

1. **Begin URI parsing:** Pinokio sees the uri `https://github.com/cocktailpeanut/llama.git/index.js`
2. **Git uri extraction:** the git repository uri is extracted from the full uri: `https://github.com/cocktailpeanut/llama.git`
3. **Git config match:** Pinokio checks if there is any top level folder under `~/pinokio/api` whose `.git/config` includes a matching remote URL
4. **Endpoint resolution:** If there's a match (let's say it finds one at `~/pinokio/api/0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974`), the resolution is complete, and the request is routed to the module inside the matched local folder (`~/pinokio/api/0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974`).
5. **Route resolution:** Now that the endpoint has been resolved, Pinokio looks at the `<relative path>` part of the full URI. In this case it's `index.js`. Pinokio takes the resolved endpoint path from the previous step (`~/pinokio/api/0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974`) and resolves the rest of the file path `index.js`, and ends up with the full local path `~/pinokio/api/0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974/index.js`.
6. **Method resolution:** Pinokio then looks at the JavaScript class file `~/pinokio/api/0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974/index.js` and finds the method `run`
7. **Method Execution:** Now that Pinokio knows which method inside which file needs to be executed, the only thing left is to actually execute the method by passing the `params` attribute. 

The `~/pinokio/api/0x68747470733a2f2f6769746875622e636f6d2f636f636b7461696c7065616e75742f6c6c616d612e676974/index.js` must follow the [API framework convention](../apps/api#api-framework), and may look something like this:

```javascript
class Llama {
  async run (request, ondata, kernel) {

    // do stuff with the request.params

  }
}
module.exports = Llama
```

The `request` parameter will contain:

```json
{
  uri: 'https://github.com/malfunctionize/llama.git/index.js',
  method: 'run',
  params: {
    message: {
      p: "### Instruction\n\nWrite a brief controversial opinion.\n\n### Response\n\n",
      m: '../models/stable-vicuna/13b_q4_0.bin',
      n: 256
    }
  },
  dirname: '/Users/x/pinokio/api/llama',
  cwd: '/Users/x/pinokio/api/llama/example',
  root: 'https://github.com/malfunctionize/llama.git/example/stable-vicuna-13b-q4_0.json',
  current: 0,
  next: null
}
```

1. `uri`: the full endpoint URI from the **begin URI parsing** step.
2. `method`: the RPC method passed in.
3. `params`: the RPC params passed in.
4. `dirname`: the resolved local path from the **endpoint resolution** step. This is the path under which the resolved module exists
5. `cwd`: the current execution path. This is the folder that contains the script that is running currently. 
6. `root`: the full path for the script file that is currently running.
7. `current`: The current instruction index within the `run` array. In this case it's 0 since it's the first instruction in the `run` array.
8. `next`: The next instruction index to be executed after the current request ends. In this case it's `null` since there is only one item in the `run` array (the current instruction), and `null` means the program will halt after this step.



# global

# global variable

The global variable is every variable prefixed with `global.`. For example:

- `global.items`
- `global.prompt`

There are a couple of ways to set the global variable:

1. [set](../api/datastructure#set): There is a dedictated method called `set` that lets you update global variables.
2. [returns](../processor/execute#returns): every step (request) can have a `returns` attribute.



# input

# input

An `input` is a special type of variable that refers to whichever data is being passed in from the request right before the current request.

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }, {
    "uri": "llama",
    "method": "run",
    "params": {
      "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
      "method": "run",
      "params": {
        "cfg_scale": 7,
        "steps": 30,
        "prompt": "{{input}}"
      }
    }
  }]
}
```

In the example above, we are:

1. making a call to the llama API to generate an animal
2. This is temporarily stored in the `input` variable when the next step is run.
3. The next step makes use of the template expression `{{input}}` to pass the generated animal name as a prompt to Automatic1111 (Stable Diffusion).

Some properties of `input`:

1. Not all methods generate return values (for example `set`), and for those methods, the `input` will be null
2. The first step in a run loop will have an `input` value of `null`.
3. The `input` value changes for every step, therefore you may often want to store the return values in the memory. For this, you can use the `returns` attributte.



# local

# local variable

The local variable is every variable prefixed with `local.`. For example:

- `local.items`
- `local.prompt`


Local variables are reset whenever the script finishes running, which means if you run a script once, and run it again, they will always start from scratch.

There are a couple of ways to set the local variable:

1. [set](../api/datastructure#set): There is a dedictated method called `set` that lets you update local variables.
2. [returns](../processor/execute#returns): every step (request) can have a `returns` attribute. The `returns` attribute is used to assign the return value to either a local variable or a global variable.



# overview

# Memory

As a pinokio script gets executed step by step, you can update the memory so it can be used in later steps.

![vacuum.jpeg](vacuum.jpeg)

1. [Input](input): (readonly) The value passed in from the previous step in the script.
2. [Local variable](local): (read and write) An in-memory variable that gets reset every time a Pinokio script finishes running. Sandboxed to the current script namespace.
3. [Global variable](global): (read and write) An in-memory variable that persists as long as Pinokio is running. When you restart Pinokio, it gets wiped out. To reset a global variable without restarting Pinokio, you can use the [rm](../api/datastructure#global-variable-1) API to reset the value.
4. [Self](self): (read and write) Variables that are accessible from memory, but also persisted to the file system. Will NOT be reset even when Pinokio restarts, since everything is stored in a file.


# self

# self

The `self` refers to the script itself.

Pinokio scripts automatically re-construct themselves every time an instruction is executed, using the following algorithm:

1. Every time an instruction in a `run` array is about to be executed, the following algorithm is run.
2. First reload the currently executing script file. (if the current script is `index.json`, Pinokio automatically reloads the file to put the up-to-date JSON object in memory)
3. Auto-import all JSON and JavaScript modules in the same folder (as well as subfolders) using the [import algorithm](#_13-import)
4. The instruction (often contains template expressions) is filled out with the resulting memory
5. The instantiated instruction is executed.


Here's an example script:

```json
{
  "run": [{
    "method": "set"
    "params": {
      "self": {
        "config.json": {
          "apikey": "blablablabll",
          "apisecret": "secretsecretsecret"
        }
      }
    }
  }, {
    "method": "log",
    "params": {
      "json": "{{self.config}}" 
    }
  }]
}
```

1. When the first instruction is run, it sets the `self.config.apikey` and `self.config.apisecret` values through the [set](../api/datastructure#set) API.
2. The next instruction prints the `self.config`, and this will be based on the most up-to-date memory state, therefore will print the following:

```json
{ "apikey": "blablablabll", "apisecret": "secretsecretsecret" }
```



# decode

# Decode

![decode.png](decode.png)

A typical Pinokio script contains template expressions.

Without template expressions, you would only be able to run static commands. What we want is to be able to dynamically form requests on the fly, so every run can run a unique request workflow based on the current state of the Pinokio state machine.

## Template

A Pinokio template expression is a string surrounded by <span v-pre>`{{ }}`</span>, and filled out on the fly when a command is run. Example:

```json
{
  "method": "set",
  "params": {
    "name": "{{input}}"
  }
}
```

So, what can go inside the <span v-pre>`{{ }}`</span> expression?

1. Any JavaScript evaluation expression: It is recommended to use only simple expressions, but any expression you can run in node.js can be included. For example: <span v-pre>`{{Buffer.from(input.images[0], "base64")}}`</span>
2. Must use the variables currently available in memory at the time of execution.

## Variables

Here are the memory variables available for filling out template expressions:

- `uri`: The request uri that triggered the script execution
- `cwd`: The current execution path
- `event`: A variable used by some API methods (such as `shell.write` or `shell.enter`)
- `input`: a value passed in from the previous step
- `local`: local variable
- `global`: global variable
- `self`: the instruction code (JSON) itself.
- `current`: the current instruction index
- `next`: the next instruction index (`null` if this is the final instruction)
- `_`: [lodash](https://lodash.com/). Includes many utility functions for dealing with data
- `os`: The [node.js os](https://nodejs.org/api/os.html) object. You can use this to determine the device platform, architecture, etc.
- `path`: The [node.js path](https://nodejs.org/api/path.html) module. You can use this to access various path related methods inside the template, such as `path.dirname()`, `path.resolve()`, etc.
- `system`: [https://github.com/sebhildebrandt/systeminformation](systeminformation module) used to get various low level system related values

### input

See [input](../memory/input)

### local

See [local variable](../memory/local)

### global

See [global variable](../memory/global)


### self

See [self](../memory/self)

### current

The `current` variable points to the index of the currently executing instruction within the `run` array. For example:

```json
{
  "run": [{
    "method": "log",
    "params": {
      "raw": "running instruction {{current}}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "running instruction {{current}}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "running instruction {{current}}"
    }
  }]
}
```

will print:

```
running instruction 0
running instruction 1
running instruction 2
```

### next

The `next` variable points to the index of the next instruction to be executed. (`null` if the current instruction is the final instruction in the `run` array):

```json
{
  "run": [{
    "method": "log",
    "params": {
      "raw": "running instruction {{current}}. next instruction is {{next}}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "running instruction {{current}}. next instruction is {{next}}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "running instruction {{current}}. next instruction is {{next}}"
    }
  }]
}
```

Above command will print the following:


```
running instruction 0. next instruction is 1
running instruction 1. next instruction is 2
running instruction 2. next instruction is null
```

### _

The `_` is the utility variable that lets you easily manipulate data inside template expressions, powered by [lodash](https://lodash.com/).

Example:

```json
{
  "run": [{
    "method": "log",
    "params": {
      "raw": "{{_.difference([2, 1], [2, 3])}}"
    }
  }]
}
```

will print:

```
1
```

Another example, where we use the `_.sample()` method to randomly pick an item from the `self.friends` variable:

```json
{
  "friends": [
    "HAL 9000",
    "Deep Blue",
    "Watson",
    "AlphaGo",
    "Siri",
    "Cortana",
    "Alexa",
    "Google Assistant",
    "OpenAI",
    "Tesla Autopilot",
    "IBM Watson",
    "Boston Dynamics",
    "IBM Deep Blue",
    "Microsoft Tay",
    "IBM DeepMind",
    "Amazon Rekognition",
    "OpenAI GPT-3"
  ],
  "run": [{
    "method": "log",
    "params": {
      "raw": "random friend: {{_.sample(self.friends)}}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "random friend: {{_.sample(self.friends)}}"
    }
  }, {
    "method": "log",
    "params": {
      "raw": "random friend: {{_.sample(self.friends)}}"
    }
  }]
}
```

Above script prints randomly picked items, for example:

```
random friend: IBM DeepMind
random friend: HAL 9000
random friend: Amazon Rekognition
```

### os

Pinokio exposes the [node.js os module](https://nodejs.org/api/os.html) through the `os` variable.

For example, ee can use the `os` variable to dynamically figure out which platform the script is running on and perhaps shape the commands based on the platform. Example:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "{{os.platform() === 'win32' ? 'dir' : 'ls'}}"
    }
  }]
}
```

Above script:

1. runs `dir` on windows
2. runs `ls` on non-windows operating systems (mac, linux)


## Timing

Instructions are decoded for every step (meaning, the template expressions are filled out on the fly when a request is about to be executed).

This means, every time an instruction is run, it is instantiated with the most up-to-date state of the state machine.

For example, the second instruction from the `run` array below is not instantiated until it's time to run it, so the <span v-pre>`{{input}}`</span> expression can be filled in using the variable `input` from the instruction right before it.

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }, {
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "{{input}}"
    }
  }]
}
```

This also means you can keep extending the instruction set WHILE the instructions are running. Here is a (somewhat convoluted) example to demonstrate how this can work:

```json
// index.json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    },
    "returns": "animal"
  }, {
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nWrite a poem about {{local.animal}}.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }, {
    "method": "goto",
    "params": {
      "index": 0
    }
  }]
}
```

1. The first instruction generates an animal name
2. The second instruction takes that animal and generates a poem
3. The third instruction loops back to index 0 (the first instruction)
4. The `local.animal` is always freshly generated for every run (because the template expression is NOT pre-filled out, but right when it's about to run)



# execute

# Execute

![execute.png](execute.png)

Once the request has been instantiated by the decoder, the request is executed.

## RPC Protocol

Every request takes the following format (an extended version of [JSON-RPC 2.0 specification](https://www.jsonrpc.org/specification)):

```json
{
  "uri": <The module path to call (optional)>,
  "method": <method name>,
  "params": <the parameters to pass to the method (optional)>,
  "returns": <return value handler (optional)>,
  "queue": <whether to queue the task or immediately run it (optional)>
}
```

Although it's an "RPC", it's used to make calls to modules that exist LOCALLY on your machine.

Even when the URI is an HTTP path, the HTTP path is merely being used to find the locally downloaded git repository whose remote URI matches the HTTP URI.


## Request Resolution

### overview

RPC, also known as "Remote Procedure Call", by design has the same expressive power as a local procedure call, meaning you can build any program using this convention.

A JSON-RPC request which looks like the following:

```json
{
  "uri",
  "method",
  "params",
  "returns",
  "queue"
}
```

is mapped to the following execution pseudocode:

```
let [RETURNS] = URI.METHOD(PARAMS)
```

### algorithm

Pinokio looks at the `uri` and `method` attributes to figure out which method to call:

#### 1. Process resolution

First, Pinokio needs to find the process using the `uri` attribute:

- **Kernel API:** A kernel API does NOT have a `uri` attribute since it's built into the Pinokio kernel.
- **Custom API:** Everything else relies on the `uri` attribute for process discoverability. If a `uri` is specified, this is used to find the relevant process.
  - **relative path:** If a relative path is used as the URI, Pinokio looks at `~/pinokio/<relative path>` to find the process file.
  - **absolute path:** If an absolute path is used (starts with `/`), it looks at that exact file location on your machine to find the process file.
  - **http git path:** If an HTTP git URI is used, Pinokio looks up all currently running processes to find the one that matches the git URI. This only applies when the process was downloaded from a remote git URL (there's a remote attribute inside the `.git/config` file)

#### 2. Method resolution

Once the process has been identified (a kernel process or a custom API process), Pinokio needs to resolve the specific method (function) within the resolved process:

- **Kernel API:** The "method" attribute refers to the corresponding kernel API.
- **Custom API:** A custom API is always a JavaScript class, which can have one or more public methods. Once the step 1 (process resolution) is successful, Pinokio can simply call the resolved object's method based on the "method" attribute name.

#### 3. Queue

Often, API calls consume a lot of CPU and memory. This is especially the case for most AI engines.

You may want to ensure that there is only one process running for each of these API endpoints at a time. For example, you may have multiple concurrent scripts running simultaneously, each of which is calling the same LLM API.

In this case, you will want to queue the tasks so only one task is running at a time for the LLM API (Instead of immediately running all tasks, which may result in concurrency, which will slow down everything)

You can use the `queue` attribute to achieve this:

```json
{
  "run": [{
    "uri": "https://github.com/malfunctionize/llama.git/index.js",
    "method": "run",
    "params": {
      "message": {
        "m": "../models/stable-vicuna/13b_q4_0.bin",
        "p": "### Instruction\n\n\rI want you to give me a random landmark location. simply write the name of the landmark location. No description. Just the name.\n\n\r### Response\n\n"
      }
    },
    "queue": true
  }]
}
```

By including the `"queue": true`, you can be sure that this API ONLY runs one task at a time, first come first served, regardless of how many scripts are running concurrently and all try to run the same API.

### example

#### Kernel API

```json
{
  "run": [{
    "method": "fs.write",
    "params": {
      "path": "temp.txt",
      "text": "hello world"
    }
  }]
}
```

Above command calls the `write()` method of the kernel's fs module.

#### Custom API

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    }
  }]
}
```

Above command looks for the running process downloaded from https://github.com/cocktailpeanut/llama.git, and calls its `run()` method.

## Response Handling

### input

By default, if a module has a return value, this return value is temporarily stored on the `input` variable, and can be used in the next instruction.

Of course, when the next instruction runs, it will generate its own return value, and the `input` variable will be overwritten with its return value.

### returns

Often you may want to store the return values so they can be used later on in the workflow. You can do that by assigning the return value to a local variable name using the `returns` attribute:


```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/llama.git/index.js",
    "method": "run",
    "params": {
      "p": "### Instruction\n\nName an animal.\n\n### Response\n\n",
      "m": "../models/stable-vicuna/13b_q4_0.bin",
      "n": 256
    },
    "returns": "local.animal"
  }, {
    . . .
  }, {
    "method": "fs.write",
    "params": {
      "json": {
        "animal": "{{local.animal}}"
      }
    }
  }]
}
```



# fetch

# Fetch

![fetch.png](fetch.png)

Pinokio adopts a [convention over configuration](https://en.wikipedia.org/wiki/Convention_over_configuration) approach in deciding which modules to load, and how.

## Resolve

The first step in every Pinokio workflow is always a URI.

1. You kick off a workflow by running a file.
2. The file needs to be either a JSON file, or a Node.js (JavaScript) module that returns JSON.

### Syntax

```json
{
  "uri": <relative path>|<absolute path>|<http git path>
}
```

### Example

The following Pinokio script runs the script at path https://github.com/cocktailpeanut/blogger.git/index.json

```json
{
  "uri": "https://github.com/cocktailpeanut/blogger.git/index.json"
}
```

### Usage

In practice, you will probably never have to call the "uri" call directly.

Instead, most often you will simply:

1. Create JSON files
2. Navigate to the JSON file URIs from Pinokio UI
3. Click "run" to run the scripts

See the next section to learn how to write Pinokio scripts.

## Load

This section explains what a typical Pinokio script file looks like.

### Requirements

Once the resolver successfully resolves a file, it checks whether

1. the JSON object contains a `run` array.
2. or in case of a node.js module, the module returns a JSON that contains a `run` array.


If above conditions pass, Pinokio loads the script for execution. The resulting JSON (The Pinokio script) is loaded into a variable named `self`. The `self` object acts as the "DNA" of a Pinokio script.

Here is an example of a valid Pinokio script:

```json
// A valid, runnable Pinokio script
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "ls -las"
    }
  }]
}
```

Here is an example of an invalid Pinokio script (Invalid scripts are ignored and not executed):

```json
// Not a runnable Pinokio script
{
  "method": "shell.run",
  "params": {
    "message": "ls -las"
  }
}
```

Above script is not a valid "runnable" Pinokio script since there is no `run` array.

### It's just JSON.

Aside from the main requirement (need to include a `run` array), there is no restriction for what you can include in a Pinokio script JSON file.

In fact, this ability to include any other attribute (not just "run") is the true power of Pinokio script---A Pinokio script can reference its OWN JSON body to run tasks. Here is an example:


```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "a pencil drawing of {{Math.floor(Math.random() * self.animals.length)}}"
    }
  }],
  "animals": [
    "elephant",
    "cat",
    "dog",
    "tiger"
  ]
}
```


Pay attention to the `run[0].params.prompt`:

```
"prompt": "a pencil drawing of {{self.animals[Math.floor(Math.random() * self.animals.length)]}}"
```

It's referencing `self.animals`, and basically generating a random animal from the `animals` array, thereby coming up with a different prompt every time.

### JavaScript support

Let's take a look at another example. This time it's a JavaScript module (instead of JSON):

```javascript
module.exports = {
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "a {{self.random(self.type)}} of {{self.random(self.animals)}}"
    }
  }],
  "type": [
    "Pencil drawing",
    "Closeup photo"
  ],
  "animals": [
    "elephant",
    "cat",
    "dog",
    "tiger"
  ],
  random: (array) => {
    let randomIndex = Math.floor(Math.random() * array.length)
    return array[randomIndex]
  }
}
```

While the recommended way to write Pinokio script is JSON (there are many benefits of using JSON, mentioned below), sometimes your use case may demand a more advanced experience.

In these cases you can write your script in a JavaScript module that exports a JavaScript object (a superset of JSON). The exported object does not need to be constrained by the JSON spec. It can even support functions, Buffers, or any data types as its value.

> The recommended way to write Pinokio script is using JSON as much as possible. This is because:
>
> 1. **Machine readable and writable:** Compared to JSON, a JavaScript code is too complicated and requires heavier reasoning to make sense of what's going on. If you express your logic in JSON as much as possible, this means the code itself is trivially machine readable therefore the code itself can change, even during execution.
> 2. **Storage friendly:** There are many database systems that support JSON based storage and queries natively. So using JSON will make your script much easier to filter and manipulate.


## Import

While it's quite cool that a single JSON can express the entire logic set AND the data that powers an intelligent autonomous AI agent, this can get messy very quickly as you add more and more attributes to the script.

To solve this problem, Pinokio lets you split out your script into as many pieces as you want. Here's how it works:

### Automatic Import

All JSON/JavaScript modules under your workspace folder are automatically imported.

Let's say we have the following Pinokio script call:

```json
{
  "uri": "myapp/index.json"
}
```

and the `myapp` folder (`~/pinokio/api/myapp`) contains the following files:

```
~/pinokio
  /bin
  /api
    /myapp
      index.json
      animals.json
      type.json
      random.js
```

And the `index.json` file looks like this:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "a {{self.random(self.type)}} of {{self.random(self.animals)}}"
    }
  }]
}
```

And `animals.json`:

```json
[
  "elephant",
  "cat",
  "dog",
  "tiger"
]
```

And `type.json`:

```json
[
  "Pencil drawing",
  "Closeup photo"
]
```

and `random.js`:

```javascript
module.exports = (array) => {
  let randomIndex = Math.floor(Math.random() * array.length)
  return array[randomIndex]
}
```

Pinokio automatically scans the `myapp` folder to find all these files and automatically attaches them to the core `index.json` file.

Therefore the attributes `self.random`, `self.type`, and `self.animals` are all made available inside `index.json` even though the `index.json` file itself does NOT contain the attributes.

Most importantly, these module imports are **automatically** carried out, so you do not need to worry about importing manually. 

To modify the behavior of the AI in your workspace, you do NOT need to restart Pinokio or manually import anything. Everything "just works" as soon as you place the files anywhere inside your workspace folder.

Any JSON file or JavaScript module will be automatically imported under the filename as attribute (without the extension)


### Recursive import

Pinokio automatically imports all the descendent folders recursively.

#### Default import

By default, the `index.json` and `index.js` files in every folder is loaded under the folder name.

For example, we could think about restructuring the folders this way:

```
~/pinokio
  /bin
  /api
    /myapp
      index.json
      /data
        index.json    # contains "animals" and "type" attributes
      /helpers
        index.js      # contains a "random" attribute that points to the random function
```

where the `myapp/data/index.json` looks like:

```json
{
  "animals": [
    "elephant",
    "cat",
    "dog",
    "tiger"
  ],
  "type": [
    "Pencil drawing",
    "Closeup photo"
  ]
]
```

and the `myapp/helpers/index.js` looks like:

```javascript
module.exports = {
  random: (array) => {
    let randomIndex = Math.floor(Math.random() * array.length)
    return array[randomIndex]
  }
}
```

This works automatically out of the box without you having to do anything. Just structure the folders that way, and the attributes will now be available under:

- `self.data.animals`
- `self.data.type`
- `self.helpers.random()`

#### Named import

This is cool, but we can go further.

Sometimes you may want to organize the modules under multiple folders AND also split them out to individual files. Let's imagine we wanted to structure the modules like the following:

```
~/pinokio
  /bin
  /api
    /myapp
      index.json
      /data
        animals.json
        type.json
      /helpers
        rarndom.js
```


Here's the modified `index.json` file that takes advantage of this new structure:

```json
{
  "run": [{
    "uri": "https://github.com/cocktailpeanut/automatic1111.git/index.js",
    "method": "run",
    "params": {
      "cfg_scale": 7,
      "steps": 30,
      "prompt": "a {{self.helpers.random(self.data.type)}} of {{self.helpers.random(self.data.animals)}}"
    }
  }]
}
```

Same as the default import, the variablees are accessible at:

- `self.data.animals`
- `self.data.type`
- `self.helpers.random()`


# overview

# Overview

![processor.png](processor.png)

The processor is the CPU of Pinokio. It follows the same scheme all modern CPUs implement ([fetch-decode-execute cycle](https://en.wikipedia.org/wiki/Instruction_cycle#Summary_of_stages))


> You can think of Pinokio as an **autonomous state machine** that loads its updated state in realtime and executes commands based on its most recent state, for every step.

1. **[Fetch (Loader)](fetch):** The loader engine instantiates the state machine (including the memory as well as `self`, which refers to its own code)
2. **[Decode (Template)](decode):** The template engine takes a template expression and instantiates it using the current state provided by the loader
3. **[Execute (Runner)](execute):** The runner takes the instantiated request and executes it.




# api

# Shell as an API

Pinokio lets you control the shell not just by writing to it, but also reading from it.

## Realtime

## Request/Response


# persistent

# Persistent shell

## You may not need a persistent shell

In most cases it's the cleanest to just run a new shell every time you run a new command, for example:

```json
{
  "run": [{
    "method": "shell.write",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui"
    }
  }, {
    "method": "shell.write",
    "params": {
      "message": "webui.bat",
      "path": "stable-diffusion-webui"
    }
  }]
}
```

## When to use a persistent shell

However sometimes you may want to keep the existing terminal session instead of starting a new one.

Some examples:

1. **Interactive session:** For example, some installer scripts require the user to interact with the command line by selecting options along the way (instead of just typing one command).
2. **Environment variable preservation:** Sometimes you may be running some command that sets up custom environment variables. In this case if you start a new shell session for every command, you will have to recreate the environment for every command. It's easier to just create one shell and keep writing to it.


```json
{
  "run": [{
    "method": "shell.write",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui"
    }
  }, {
    "method": "shell.write",
    "params": {
      "message": "webui.bat",
      "path": "stable-diffusion-webui"
    }
  }]
}
```


# run

# Run Anything

Pinokio comes with various APIs, but one of its most useful APIs is the **shell API**.

The shell API lets you write a script that automatically runs anything on your machine.




# wait

# Wait for event

Often when running commands, they don't end immediately and you will have to wait for it to end before going to the next step.

In this case you need to declare event handlers with an "on" array.

Here's an example:

```json
{
  "run": [{
    "method": "shell.write",
    "params": {
      "message": "curl https://jsonplaceholder.typicode.com/users",
      "on": [{
        "event": "/.*(\\[.*\\]).*/gs",
        "return": "{{event.matches[0][1]}}"
      }]
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "users.json",
      "text": "{{input}}"
    }
  }]
}
```


# api

# Build your own API

If you reached this far, you are already able to do all kinds of powerful things simply by writing JSON scripts:

1. make network requests
2. manipulate files
3. store and retreive data
4. run any command on your machine
5. etc.

All of these features are possible thanks to the **built-in Pinokio native APIs**. But often you may want to go further and even write and publish your OWN APIs. Use cases include:

1. Integrating with 3rd party APIs
2. Packaging powerful workflows into their own simple APIs (like the native Pinokio APIs)

To learn more about writing your own APIs, check out the [Build your own API section](/custom/what)


# autostart

# Self driving scripts

By default you need to click "Run" (or invoke them programmatically) to run a script.

But often you may want certain scripts to automatically run themselves whenever Pinokio rstarts.

For example if your script involves starting a server, you would probably want the server to automatically start whenever Pinokio starts.

Otherwise you would have to manually start all the servers required to run your scripts every time you restart Pinokio.

You can configure this by placing a special purpose file named `pinokio.js` in your project home directory. Let's imagine a project folder called `myscript`:


```
~/pinokio
  /api
    /myscript
      install.json
      start.json
```

We want Pinokio to automatically run `~/pinokio/api/myscript/start.json` whenever it restarts.

## pinokio.json

All we need to do is to create a file named `pinokio.js` and return a JSON object with its `start` attribute pointing to the start script file. Here's an example `pinokio.js` file:

```javascript
// pinokio.js
module.exports = {
  "start": "start.json"
}
```

The resulting file structure will look like this:

```
~/pinokio
  /api
    /myscript
      pinokio.js
      install.json
      start.json
```

Now when you restart Pinokio, Pinokio will automatically run the `start.json` script at the beginning.

## dynamic start script

Sometimes you may not want to trigger the start script until some condition is met.

For example, your `start.json` script may involve launching a web server, but this only makes sense when the web server is fully set up, or installed.

In this case, instead of setting a static value for the `start` attribute, the start attribute can be a JavaScript async function that returns the value:

```javascript
// pinokio.js
module.exports = {
  "start": async (kernel) => {
    
    // Run some logic here to check if all the modules have been installed
    //
    // . . . .
    //

    if (installed) {
      return "start.json"
    }
  }
```


# database

# Installing a DB automatically

TBD


# dependencies

# Declaring dependencies

Often your app may depend on 3rd party APIs. For example imagine an autonomous blogger app, which generates paragraphs and images with AI, and publishes the content to Tumblr.

This app may utilize:

1. **LLaMA API:** for LLM text generation
2. **StableDiffusion API:** for image generation
3. **Tumblr post API:** for posting to Tumblr.com

When publishing your app, you can include the links in your `README.md` file so people can download them one by one.

But this is such a common feature that Pinokio has this built in.

In addition to including the links in the README file, you can use the `dependencies` array in the `pinokio.js` file to declare all the APIs one must install before using your app.

Here's an example `pinokio.js` file:

```javascript
// pinokio.js
module.exports = {
  menu: [{
    html: "<i class='fa-solid fa-plug'></i> Install",
    href: "install.json"
  }],
  start: "start.js",
  dependencies: [
    "https://github.com/malfunctionize/llama.git",
    "https://github.com/malfunctionize/automatic1111.git",
    "https://github.com/malfunctionize/tumblr.git"
  ]
}
```

When this repository is downloaded and loaded on Pinokio, the user will see the following screen:

![download.png](download.png)

When you click the download buttons, they will open in a new Pinokio window, where you can download and install these APIs.

Once all the APIs have been downloaded, refresh the page and you will see that the "download" buttons are gone and replaced with check marks to indicate that these dependencies have been downloaded:

![downloaded.png](downloaded.png)

Once all the dependencies have been installed, you can install the current app itself.

![downloaded2.png](downloaded2.png)


# document

# Documenting

There are a couple of ways to implement user interface in your scripts.

The simplest way is to use the `README.md` files to document each folder.

Pinokio will automatically render the README.md file for each folder, and here you can explain how your script works, as well as include links to the scripts.


# dynamic

# Dynamic Scripting

There are multiple ways you can use JavaScript to **dynamically construct the JSON script**.

1. **JavaScript inside JSON:** Evaluating JavaScript inside JSON
2. **JSON from JavaScript:** Evaluating JavaScript to dynamically return JSON
3. **Raw mode:** Not Evaluating anything

## JavaScript inside JSON

> This option is the recommended way to dynamically construct JSON in most cases.
>
> Only use other methods if you can't use this method to dynamically generate JSON.

Pinokio script supports a dynamic template feature that automatically fills out the template expressions at runtime.

> Learn more about templates [here](/processor/decode#template)

Here's an example using the `os` variable in a template expression and running different commands depending on the OS:

```json
{
  "run": [{
    "method": "goto",
    "params": {
      "index": "{{os.platform() === 'darwin' ? 1 : 5}}"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "brew install cmake protobuf rust python@3.10 git wget"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui automatic1111"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "sh webui.sh -f --api",
      "path": "automatic1111"
    }
  }, {
    "method": "goto",
    "params": {
      "index": null
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui automatic1111"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "{{os.platform() === 'win32' ? 'webui-user.bat' : 'bash webui.sh -f --api'}}",
      "path": "automatic1111"
    }
  }]
}
```

0. It first checks if the OS is `darwin` (mac) or not.
1. If it's a mac, it jumps to instruction 1 with the `goto` method
    - which runs the `brew install` command (instruction 1),
    - followed by `git clone` (instruction 2),
    - followed by `sh webui.sh -f --api` (instruction 3),
    - and finally finishes the script with `{ "method": "goto", "params": { index: null } }`
2. If it's not a mac, it jumps to instruction 5 with the `goto` method
    - wich runs `git clone` (instruction 5)
    - followed by checking the os (instruction 6)
    - and if the os is `win32`, runs `webui-user.bat` (instruction 6)
    - if the os is NOT `win32` (linux), runs `bash webui.sh -f --api` (instruction 6)


## JavaScript to return JSON

By default, Pinokio interprets a static JSON file to run instructions.

But sometimes you may want to dynamically generate the JSON script itself, using JavaScript.

To do this, just write a node.js module that returns a JSON object dynamically.

Here's the same example that takes operating systems into account, and exports custom Pinokio script JSON depending on the context:

```javascript
const os = require('os')
const platform = os.platform()
let cmd
if (platform === 'win32') {
  cmd = "webui-user.bat"
} else if (platform === 'darwin') {
  cmd = "sh webui.sh -f --api"
} else {
  cmd = "bash webui.sh -f --api"
}
let general = {
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui automatic1111"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": cmd,
      "path": "automatic1111"
    }
  }]
}

let mac = {
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "brew install cmake protobuf rust python@3.10 git wget",
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui automatic1111"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": cmd,
      "path": "automatic1111"
    }
  }]
}

let x
if (platform === "mac") {
  x = mac
} else {
  x = general
}
module.exports = x
```

## Raw mode

Sometimes you may need to use template expressions but without evaluating them.

In this case you can use three curly brackets:

```
{{{ expression }}}
```

When you include expressions in a raw mode temlate, it will be unwrapped once and turn into a template expression that can be evaluated next time you try to evaluate.

Let's take a look at an example to see when this can be useful. Let's imagine we want to write a Pinokio script to a file using Pinokio script.

The problem is, this script includes a template expression, like this:

```json
{
  "run": [{
    "method": "shell.run",
    "params": "{{ os.platform() === 'win32' ? 'dir' : 'ls' }}"
  }]
}
```

if we naively try to do this, it will look something like this:


```json
{
  "run": [{
    "method": "fs.write",
    "params": {
      "path": "script.json",
      "json2": {
        "run": [{
          "method": "shell.run",
          "params": "{{ os.platform() === 'win32' ? 'dir' : 'ls' }}"
        }]
      }
    }
  }]
}
```

But we may end up with an unexpected behavior. If we run the code above, the template expression will be evaluated when the `fs.write` method is called, therefore the template expression will be evaluated instead of literally being written to the file.

We will end up with a `script.json` file that looks like this:

```json
{
  "run": [{
    "method": "shell.run",
    "params": "ls"
  }]
}
```

or in case of windows:

```json
{
  "run": [{
    "method": "shell.run",
    "params": "dir"
  }]
}
```

So how do we avoid this evaluation and write the template expression literally to the file?

This is where the **raw mode** comes in:

```json
{
  "run": [{
    "method": "fs.write",
    "params": {
      "path": "script.json",
      "json2": {
        "run": [{
          "method": "shell.run",
          "params": "{{{ os.platform() === 'win32' ? 'dir' : 'ls' }}}"
        }]
      }
    }
  }]
}
```

Note that the template expression is wrapped with **3 curly brackets**.

When this script is run, the raw template expression will not be evaluated, but instead be unwrapped and turn into a template expression before being written to the file, and we would end up with the desired `script.json` file that looks like this:

```json
{
  "run": [{
    "method": "shell.run",
    "params": "{{ os.platform() === 'win32' ? 'dir' : 'ls' }}"
  }]
}
```


# enter

# Auto-press Enter

Since `shell.write` does NOT automatically press the "enter" key for you, when you're trying to run commands with `shell.write` you will need to append all your messages with `\n`, for example:

```json
{
  "run": [{
    "method": "shell.write",
    "params": {
      "message": "{{os.platform() === 'win32' ? 'dir' : 'ls'}}\n"
    }
  }]
}
```

There are two things to note here:

1. First, we're using [template expressions](/processor/decode#template) and the built-in `os` variable to determine the platform and sending `dir` if windows, and `ls` if otherwise.
2. Second, the `message` ends with an explicit `\n` (newline character).

If you don't include the `\n` at the end, it will just print `dir` or `ls` and not run them.

Since most use cases will involve entering commands and it will get tedious to append everything with `\n`, Pinokio also provides a method called `shell.enter`.

The `shell.enter` command basically does the same thing as `shell.write`, except it always automatically enters the enter key for you at the end.

Above example can be transformed to the following (Notice we're using `shell.enter` instead of `shell.write`, and that the trailing `\n` in the `message` is gone now):


```json
{
  "run": [{
    "method": "shell.enter",
    "params": {
      "message": "{{os.platform() === 'win32' ? 'dir' : 'ls'}}"
    }
  }]
}
```


# env

# Custom envrionment variables

Often, programs require setting custom environment variables for the execution context. Some examples:

1. **Server Configuration:** For example, Automatic1111 (StableDiffusion) lets you set the environment variable `COMMANDLINE_ARGS` to customize how the stable diffusion web ui is configured.
2. **API Keys:** Many apps do NOT store private secrets and API keys in the code but lets you pass them in through environment variables (example: `OPENAI_API_KEY`, etc.)

The shell API lets you specify custom environment variables as well (This example uses a fake API key).

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "npm start",
      "env": {
        "OPENAI_API_KEY": "sk-r2v42ad3f8s3hfslgh3skdhgl3ksdhbh3ks34t23djgFdDa"
      }
    }
  }]
}
```

1. It runs the `npm start` command
2. But also passes in the `env` attribute, which sets the `OPENAI_API_KEY` variable when executing `npm start`.


# forms

# Form

Everything in Pinokio is JSON.

You can configure everything by simply opening the JSON files, updating, and saving:

![json.png](json.png)

But sometimes you may want to provide an easy-to-use UI for end users, so they can play with data easily **without having to directly tweak the JSON files**. Here's an example:

![form.png](form.png)

## How to generate a form

Pinokio provides an easy way to automatically generate forms like this for any JSON file. You can achieve this using the built-in form builder engine. Here's how it works:

1. Pick a JSON you want to generate a form for.
2. Create a JSON schema for the JSON.
3. Save the schema with a filename expected by Pinokio (Just add a `_` prefix to the original filename)
4. Now when you open the original JSON file, it will display the form view instead of the raw JSON.

For example, we havea `tumblr.json` file that we want to turn into a form:

![json.png](json.png)

We can do this by simply creating a file named `_tumblr.json` (note the `_` prefix) in the same folder and saving the JSON schema for the `tumblr.json` file:

![schema.png](schema.png)

Now when we visit the `tumblr.json` file, instead of the raw JSON view, we get the form view:

![form.png](form.png)

You can click the **View Source** button to switch to the JSON view.

## Getting a JSON schema

![schemagen.png](schemagen.png)

You can easily create a JSON schema from any JSON.

For example you can just use web apps like https://transform.tools/json-to-json-schema to enter any JSON and it will automatically generate a basic schema for you.

You can customize further on top of the basic schema if you want.

## Examples

### Case Study: Data Forms

Let's say we have an array stored at `animals.json`:

```json
[
  "Aardvark",
  "Ant",
  "Antelope"
]
```

And we want people to be able to edit this list WITHOUT touching the raw JSON, but through a form.

Just create a JSON schema file for `animals.json`, named `_animals.json`, in the same folder:

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "animals",
  "type": "array",
  "items": {
    "type": "string",
    "title": "animal"
  }
}
```

Now when you open the `animals.json`, it will display the form view by default.

### Case Study: Config Forms

Another useful case is when you need to configure some engines, such as API clients.

Instead of making users manually edit JSON, you can auto-generate a form to set all the configuration fields.

Let's say we have built a tumblr API client script, and it requires the `tumblr.json` to be filled out before using:

```json
{
  "name": "",
  "config": {
    "consumer_key": "",
    "consumer_secret": "",
    "token": "",
    "token_secret": ""
  }
}
```

We can create a JSON schema file for `tumblr.json`, which will look like this:


```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "tumblr",
  "type": "object",
  "properties": {
    "required": [
      "name", "config"
    ],
    "name": {
      "type": "string",
      "title": "tumblr name"
    },
    "config": {
      "type": "object",
      "properties": {
        "required": [
          "consumer_key",
          "consumer_secret",
          "token",
          "token_secret"
        ],
        "consumer_key": {
          "type": "string"
        },
        "consumer_secret": {
          "type": "string"
        },
        "token": {
          "type": "string"
        },
        "token_secret": {
          "type": "string"
        }
      }
    }
  }
}
```

And now when the users open `tumblr.json`, they will get the form view, which is much easier to work with.



# hello

# Hello world

Let's start by creating a simple script that lists files in the current directory.

When run, this script will run "ls" (or "dir" on windows)

![helloworld.gif](helloworld.gif)

First, find the [API folder under the Pinokio file system](/fs/overview.html#api). The folder structure will look something like this:


```
~/pinokio
  /api
  /bin
```

To create a project folder, go into `~/pinokio/api` and create a new folder named `helloworld`


```
mkdir helloworld
```

The resulting folder structure will be:

```
~/pinokio
  /api
    /helloworld
  /bin
```

Now create a script file named `index.json` inside the `~/pinokio/api/helloworld` folder:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "ls"
    }
  }]
}
```

Or, if you're on Windows, use `dir` instead:


```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "dir"
    }
  }]
}
```

The folder structure would look something like this:

```
~/pinokio
  /api
    /helloworld
      index.json
  /bin
```

Now open Pinokio and you will see the `helloworld` folder on the home page.

1. Go to the `helloworld/index.json` page
2. Click the **Run** button at the top.
3. You will see the command being executed and the web terminal display the result.


# index

# Getting started

This section is a growing list of tutorials that will help you understand how to write scripts for Pinokio.

> **It is not required but recommended that you read them in this order.**

1. [Hello world](hello): Write a minimal script that runs a shell command.
2. [Run multiple scripts](multiple): Automatically run multiple commands in sequence.
3. [Automatically type keys](write): Have full control over the shell by programmatically typing keys.
4. [Pressing enter](enter): Learn the difference between entering commands and typing keys.
5. [Interacting with the shell](programming): In addition to writing to the shell, learn how to read and process the realtime data from the shell, treating the shell like a server.
6. [Run python scripts](python): Write a simple Pinokio script that automatically runs python scripts.
7. [Custom environment variables](env): Learn how to run shell environments with custom environment variables.
8. [Self driving scripts](autostart): Learn how to make your scripts automatically run without human intervention.
9. [Custom menu bar](menu): Learn how to customize the menubar for your script repository.
10. [Install a DB automatically](database): Learn how to install and populate a database autonomously.
11. [Documenting scripts](document): Script documentation tips
12. [Dynamic scripts](dynamic): How to generate Pinokio scripts dynamically.
13. [Declaring dependencies](dependencies): How to display an install menu for downloading dependencies for your scripts.
14. [User-friendly forms](forms): How to auto-generate forms for filling out any JSON.
15. [Publishing scripts](publish): How to publish and share Pinokio scripts.


# menu

# Custom menu bar

By default, the top menu bar displays an "Update" button, which when clicked, pulls in updates from the git repository from which the code was downloaded.

## pinokio.json

But you can add additional custom buttons to the menu with `pinokio.js`, for example include a link to an install script, like this:

<p>
<img src="./install.png" class='framed'>
</p>

To achieve this, simply create a file named `pinokio.js` and add items to the `menu` array:

```javascript
module.exports = {
  menu: [{
    html: "<i class='fa-solid fa-plug'></i> Install",
    href: "install.json"
  }]
}
```

Each menu item can have the following attributes:

- `html`: The html code for the item content
- `href` (optional)
  - If specified, renders a button that links to the `href` URL.
  - If not specified, renders a label.

## dynamic menu construction

Sometimes you may want to dynamically generate the menu items instead of always having the same menu.

In this case, instead of setting an array for the `menu` attribute, the menu attribute can be a JavaScript async function that returns an array.

Example:

```json
module.exports = {
  menu: async (kernel) => {

    // Run some logic here to check if all the modules have been installed
    //
    // . . . .
    //

    if (installed) {
      // 1. is it installed already? => display an "installed" label
      return [{
        "html": "Installed"
      }]
    } else {
      // 2. is it not installed? => display an install button
      return [{
        "html": "<i class='fa-solid fa-plug'></i> Install",
        "href": "install.json"
      }]
    }
  }
}
```


# multiple

# Run multiple commands

In this tutorial we will write a script that runs multiple commands in sequence.

More specifically, just with one click, our script will:

1. Initialize a new NPM project
2. Install the `express` NPM package (a web server library)
3. Write a JavaScript code for the web server
4. Spin up the express server

100% automatically.

![helloserver.gif](helloserver.gif)

Let's try creating an example.

Create a folder named `helloserver` and create a file named `index.json`:

```
~/pinokio
  /api
    /helloworld
      index.json
    /helloserver
      index.json
  /bin
```

The `index.json` should look like this:

```json
{
  "run": [{
    "method": "shell.run",
    "params": {
      "message": "mkdir engine"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "npm init -y",
      "path": "engine"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "npm install express",
      "path": "engine"
    }
  }, {
    "method": "fs.write",
    "params": {
      "path": "engine/index.js",
      "text": [
        "const express = require('express');",
        "const app = express();",
        "app.get('/', function (req, res) {",
        "  res.send('<h1>Hello World</h1>');",
        "});",
        "console.log('starting server')",
        "app.listen(3000, () => { console.log ('server started') });"
      ],
      "join": "\n"
    }
  }, {
    "method": "shell.run",
    "params": {
      "message": "node index",
      "path": "engine"
    }
  }]
}
```

1. The first step runs `mkdir helloserver` to create a folder named `helloserver`
2. The second step runs `npm init -y` to initialize an NPM project
3. The third step runs `npm install express` to install the [express.js](https://expressjs.com/) package, which we will use to build a super simple web server.
4. The fourth step uses an API called [fs.write](/api/fs) to write lines to the file named `helloserver/index.js`
5. The final step runs `node index` to start the express server code we just wrote through the `fs.write` API.

At this point your `helloserver` project folder will look something like this:

```
~/pinokio
  /api
    /helloworld
      index.json
    /helloserver
      index.json
      /engine
        package.json
        index.js
        /node_modules
  /bin
```

Now go to `http://localhost:3000` and you will see the web server is up and displaying "Hello World".




# programming

# Interacting with the shell

Simply being able to send off commands to the terminal is not enough if you want to fully control what happens in the terminal.

Often you will need to:

1. **Read and Process:** Read and process realtime data from the terminal (instead of just writing to it)
2. **Wait:** Wait for certain pattern to occur before returning

The event handler (The `on` attribute) lets you achieve this (available with `shell.write` and `shell.enter`).

Let's imagine we want to build an autonomous intelligence that can **install and run programs**.

Often, installing or setting up libraries and packages require an interactive session. Take `npm init` for example. When you run the command, it will get into an interactive mode where the user needs to enter stuff multiple times in order to complete the setup.

Here's an example of what happens when you run `npm init`:

```
> npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (myapp)
```

From this point, the user needs to either press "enter" to fill out the attribute with default values, or enter custom values.

If you keep pressing `enter`, the initialization process will keep filling out the required attributes with the default values and eventually end, and the control will return back to the prompt:

```
> npm init
This utility will walk you through creating a package.json file.
It only covers the most common items, and tries to guess sensible defaults.

See `npm help init` for definitive documentation on these fields
and exactly what they do.

Use `npm install <pkg>` afterwards to install a package and
save it as a dependency in the package.json file.

Press ^C at any time to quit.
package name: (yyy)
version: (1.0.0)
description:
git repository:
author:
license: (ISC)
About to write to /Users/x/Demos/yyy/package.json:

{
  "name": "yyy",
  "version": "1.0.0",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "description": ""
}
> 
```

In this example, we're going to automate this entire `npm init` process using Pinokio, by automatically walking through the entire `npm init` workflow step by step, by simply submitting `enter`:


```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.enter",
    "params": {
      "message": "npm init",
      "on": [{
        "event": "/.+: /",
        "return": true
      }]
    }
  }, {
    "method": "shell.enter",
    "params": {
      "message": "",
      "on": [{
        "event": "/.+: /",
        "return": 2
      }, {
        "event": null,
        "return": null
      }]
    }
  }, {
    "method": "goto",
    "params": {
      "index": "{{input}}"
    }
  }]
}
```

1. First we start a shell session with `shell.start`
2. Then we run `npm init` with `shell.enter`
    1. The entered `message` is `""`. The `shell.enter` will simply press enter in this case.
    2. Note that we have an `on` event handler array. The `on` array can contain as many event handlers as you want but in this case we only have one handler.
    3. The event handler waits for a regular expression `/.+: /` to be printed on the terminal. And when it does, it returns `true`.
    4. In this case, the `/.+: /` event will trigger when it first reaches the `package name: (myapp)` part of the `npm init` execution since it matches the regular expression.
3. Then it goes onto the next step, where it again submits an empty string `""`
    1. This time we have 2 event handlers, executed sequentially.
    2. The first event handler is the same `.+: /` handler, which indicates that we are still in the `npm init` session. This returns 2 (which will be used in the next step)
    3. The second event handler is `event: null`. This is a special event that gets triggered when the terminal encounters a new terminal prompt. In this case it will be `> ` (as shown above), and in this case returns `null`
4. Finally the last step is a `goto` statement, which utilizes the `input` (passed in from the previous step as the return value).
    1. In case of the `/.+: /` pattern, we know we're still in the `npm init` process so it goes to the index 2, which keeps submitting enter keys.
    2. In case of the `null` event, we know we've encountered a terminal prompt, so we need to finish the script. The `goto` method with `index: null` ends the script.

Let's step back and appreciate what we have built.

**We have built something that can write, read, and process anything in terminal, without human intervention.**



# publish

# Publishing Scripts

Scripts are powerful but they are even more powerful when they are shared with the world, since everyone can download and run the same workflow with one click.

There are a couple of things to note:

1. **Include an Example:** Package an example along with the API if possible. It's nice to be able to install an API and immediately try it out. You can set up a separate example repository, or include it in the same API folder.
2. **Publish to GitHub:** Publish to GitHub. You can publish to other git hosting services as well, but GitHub recommended for now [for discoverability](#list-on-pinokio).
3. **List:** When publishing to GitHub, tag your repository with `pinokio`, and it will automatically show up inside the Discover page in the Pinokio app.


## Include a README

Just like how GitHub automatically renders README.md files for any git repository, Pinokio also renders the `README.md` files. All you need to do is include the file in the root folder of your API repository.

a README documentation helps users easily use your API, so be as descriptive as possible.

## Include some examples

Also, it's great to include some example scripts, so the users who download your API can try out the API instantly without them having to write their own script to test.

For example,

1. just create an `example` folder and include the example scripts under the folder
2. link to the example scripts from `README.md`

Or if you want just a simple script, you can just create one `example.json` in the root folder. Choice is up to you.


## Publish to GitHub

Finally we're ready to publish.

There's nothing special here, just publish the repository to GitHub just like you publish any repository.

## List on Pinokio

![discover.png](discover.png)

Pinokio has a "discover" page which displays all the public Pinokio APIs published on GitHub.

To list your published API on the Pinokio discover page, just tag your repository with "pinokio", and it should immediately show up on the discover page:

![tagging.gif](tagging.gif)



# python

# Running python scripts

Let's zoom out and think about what all this means:

1. You can pretty much control ANYTHING on your computer with terminal.
2. You can control COMPLETELY control terminal with Pinokio shell.
3. This means you can control anything on your computer with pinokio.

To emphasize this concept, let's write a simple python script, which then can be controlled with Pinokio script.

1. We will write a python script that takes a string as an argument, and prints a reversed version of it on the terminal.
2. Then we will run this python script using Pinokio script.

![python.gif](python.gif)

First create a python file named `reverse.py`:

```python
import sys
def reverse(input_string):
    return input_string[::-1]
print("<pinokio>" + reverse(sys.argv[1]) + "</pinokio>")
```

This program takes a command line argument, reverses the string, and returns the value wrapped with `<pinokio> ... </pinokio>` (Just so it's easier to process the pattern from the Pinokio side.

Now let's write a Pinokio script that runs this python script. Create a file named `run.json` in the same folder:


```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.enter",
    "params": {
      "message": "python reverse.py helloworld",
      "on": [{
        "event": "/<pinokio>(.+?)<\/pinokio>/",
        "return": "{{event.matches[0][1]}}"
      }]
    }
  }, {
    "method": "notify",
    "params": {
      "html": "{{input}}"
    }
  }]
}
```

1. It creates a shell session (`shell.start`)
2. Runs the `python reverse.py helloworld` command (`shell.enter`)
3. Waits for the `/<pinokio>(.+?)</pinokio>/` regular expression event
4. When it does, it parses the matched part and returns it (`event.matches[0][1]` is the first item in the capture group from the first match)
5. Then we call the `notify` method to display a push notification with the reversed string `{{input}}`




# run

# Run anything

The `shell` API is a JSON-RPC endpoint that lets you fully control your machine's shell over local HTTP requests.

With the access to the shell you can do anything you can imagine. Some examples:

1. **Run commands:** Run batch scripts and shell scripts
2. **Install anything:** One-click install anything (pip install, node install, conda install, etc)
3. **Download and upload anything:** clone or push git repositories.
4. **Write files:** write, copy, remove files
5. etc.





# script



# share

# Sharing Scripts

Pinokio has a built-in URI scheme that lets you share **one-click install links** to your Pinokio scripts.

![deeplink.gif](deeplink.gif)


```
pinokio://?mode=download&url=<git url>
```

Here is an example:

[pinokio://?mode=download&url=https://github.com/malfunctionize/kerneldemo.git](pinokio://?mode=download&url=https://github.com/malfunctionize/kerneldemo.git)



# write

# Enter keystrokes

While you can already achieve a lot of things by simply running one-off commands with `shell.run`, this may not be enough for more advanced cases where you need more fine grained access to the shell.

For example instead of simply running commands, you may neeed to:

1. Enter keystrokes one by one.
2. Keep the shell running instead of just running one command and halt.
3. Monitor and handle events in the shell.
4. Return values from the shell

In this tutorial, we will write a script that automatically enters keystrokes:

![keystrokes.gif](keystrokes.gif)

We can achieve this by using:

1. `shell.start`: to create a new shell session.
2. `shell.write`: to write to the created shell session.

Let's try entering keystrokes to the shell. This example will simply loop forever and keep entering a random number into the terminal every 1 second.

```json
{
  "run": [{
    "method": "shell.start"
  }, {
    "method": "shell.write",
    "params": {
      "message": "{{String(Math.floor(10 * Math.random()))}}",
      "on": [{
        "event": "/.*/",
        "return": true
      }]
    }
  }, {
    "method": "process.wait",
    "params": {
      "sec": 1
    }
  }, {
    "method": "goto",
    "params": {
      "index": 1
    }
  }]
}
```

Here's how it works:

1. First we start a shell with `shell.start`
2. Then we call `shell.write` to write the `params.message` to the shell. In this case the expression `{{String(Math.floor(10 * Math.random()))}}` means we are randomly generating a number between 0 and 10 and entering the number to the terminal (without pressing enter)
3. The `params.on` is the event handler that waits for the `/.*/` pattern (which matches any character) and returns `true`. This means this command will write the random number to the terminal and immediately return.
4. Then it goes to the next step where it runs `process.wait` with `sec: 1`, which pauses for 1 second.
5. Then it goes on to the next step where it runs "goto 1", which loops back to the `shell.write` instruction at position 1.
6. The script loops forever, printing a random number to the terminal every one second.



