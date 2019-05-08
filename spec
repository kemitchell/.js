Here is the grammar for tags:

A tag name consists of an ASCII letter followed by zero or more ASCII letters, digits, or hyphens (-).

An attribute consists of whitespace, an attribute name, and an optional attribute value specification.

An attribute name consists of an ASCII letter, _, or :, followed by zero or more ASCII letters, digits, _, ., :, or -. (Note: This is the XML specification restricted to ASCII. HTML5 is laxer.)

An attribute value specification consists of optional whitespace, a = character, optional whitespace, and an attribute value.

An attribute value consists of an unquoted attribute value, a single-quoted attribute value, or a double-quoted attribute value.

An unquoted attribute value is a nonempty string of characters not including whitespace, ", ', =, <, >, or `.

A single-quoted attribute value consists of ', zero or more characters not including ', and a final '.

A double-quoted attribute value consists of ", zero or more characters not including ", and a final ".

An open tag consists of a < character, a tag name, zero or more attributes, optional whitespace, an optional / character, and a > character.

A closing tag consists of the string </, a tag name, optional whitespace, and the character >.

An HTML comment consists of <!-- + text + -->, where text does not start with > or ->, does not end with -, and does not contain --. (See the HTML5 spec.)

A processing instruction consists of the string <?, a string of characters not including the string ?>, and the string ?>.

A declaration consists of the string <!, a name consisting of one or more uppercase ASCII letters, whitespace, a string of characters not including the character >, and the character >.

A CDATA section consists of the string <![CDATA[, a string of characters not including the string ]]>, and the string ]]>.

An HTML tag consists of an open tag, a closing tag, an HTML comment, a processing instruction, a declaration, or a CDATA section.
