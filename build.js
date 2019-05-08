#!/usr/bin/env node

// An open tag consists of a < character, a tag name, zero or more
// attributes, optional whitespace, an optional / character, and a >
// character.

var openTag = '<' + tagName() + attributes() + optionalWhitespace() + optionalSlash() + '>'

// A closing tag consists of the string </, a tag name, optional
// whitespace, and the character >.

var closingTag = '</' + tagName() + optionalWhitespace() + '>'

// A tag name consists of an ASCII letter followed by zero or more ASCII
// letters, digits, or hyphens (-).

function tagName () {
  return '([A-z][A-z0-90-]*)'
}

var output = {}

console.log(JSON.stringify(output, null, 2))
