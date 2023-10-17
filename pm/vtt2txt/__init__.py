import re


NUM_RE = re.compile(r"^\d+$")
TIME_RE = re.compile(r"^[\d:.]+ --> [\d:.]+$")
TAG_RE = re.compile(r"<.*?>")
SENTENCE_END_RE = re.compile(r'''
    ( [.?!] "? )    # Sentence-ender with optional end quote
    [ ] +           # At least one space character
''', re.VERBOSE)


def rewrap(text):
    """Rewrap text to have one sentence per line."""
    sentences = []
    current_sentence = []
    for line in text.splitlines():
        line = line.strip()
        line_sections = []
        for item in SENTENCE_END_RE.split(line):
            if line_sections and item.startswith((".", "?", "!")):
                line_sections[-1] += item
            else:
                line_sections.append(item)
        match line_sections:
            case [continued]:
                current_sentence.append(continued)
            case [continued, *other_sentences, new_sentence]:
                current_sentence.append(continued)
                sentences.append(" ".join(current_sentence))
                sentences.extend(other_sentences)
                current_sentence = [new_sentence]
        if line.endswith((".", "?", "!")):
            sentences.append(" ".join(current_sentence))
            current_sentence = []
    return "\n".join(sentences)


def strip_tags(text):
    """Strip markup tags."""
    return TAG_RE.sub(r"", text)


def just_text(vtt_text):
    """Yield the text lines from each group."""
    vtt_text = (
        vtt_text.strip()
        .lstrip("\ufeff")
    )
    if vtt_text.startswith("WEBVTT"):
        vtt_text = vtt_text[len("WEBVTT"):]
    vtt_text = vtt_text.strip()
    for group in re.split(r"\n{2,}", vtt_text):
        for line in group.splitlines():
            if NUM_RE.search(line) or TIME_RE.search(line):
                continue
            yield strip_tags(line)


def vtt_to_text(vtt_text):
    """Convert VTT file text to plain text"""
    return rewrap("\n".join(just_text(vtt_text)))
