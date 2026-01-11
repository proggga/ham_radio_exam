# Ham Radio Exam Zettelkasten

This is a **Zettelkasten** (slip-box) knowledge base for the Ham Radio Full License exam. Unlike traditional documentation, this system consists of atomic, interconnected notes that form a web of knowledge.

## System Structure

*   **Atomic Notes:** Each file contains a single concept or idea.
*   **Clean Filenames:** Files are named clearly describing their content (e.g., `Atomic Theory.md`) WITHOUT IDs in the filename.
*   **Frontmatter:** Each note contains metadata (ID, title, tags, creation date, type) in YAML format at the top. IDs are stored here, not in the filename.
*   **Bidirectional Linking:** Notes link to each other to create a knowledge graph. Use `[[WikiLinks]]`.

## How to Navigate

*   **[Master Index](zettelkasten/Master%20Index.md):** The main entry point listing all topics categorized by the syllabus.
*   **Tags:** Use your IDE's search to find notes by tags (e.g., `#ham-radio`, `#electricity`).
*   **Graph View:** If your editor supports it (like Obsidian or VS Code with Markdown links), use the Graph View to visualize connections.

## Note Types

*   **Permanent Notes:** The core content (Theories, Components, [Regulations](zettelkasten/Rules%20&%20Regulations.md)).
*   **Index / Map of Content (MOC):** Structure notes that organize other notes.

## Adding New Notes

1.  Create a new file with a clear, descriptive name: `Concept Name.md`.
2.  Add the standard frontmatter (you can use `zettelkasten/templates/zettel-template.md`):
    ```yaml
    ---
    title: "Concept Name"
    tags: ["ham-radio", "topic"]
    created: 2025-12-29
    modified: 2025-12-29
    type: permanent-note
    id: 202512291200
    ---
    ```
3.  Write your atomic content. Focus on **one** idea per note.
4.  Link to other related notes using `[[Related Note]]`.
5.  Add the note to the [Master Index](zettelkasten/Master%20Index.md) or a relevant Map if appropriate.

## Linking Rules

*   **Rich Linking:** Aim for 5-10 links per note.
*   **Inline Links:** Link concepts as you mention them: "This uses a [[Resistor]] to limit current."
*   **Related Section:** Add a "Related Notes" section at the bottom for connections that don't fit inline.

## Maintenance Tools

*   **`find_orphans.py`**: Runs a check to ensure every note (except the Master Index) is linked from at least one other note. Use this to enforce the "No Orphans" rule.
*   **`generate_study_guide.py`**: Compiles all notes into a linear Study Guide in the `docs/` folder, organized by the Master Index structure.
