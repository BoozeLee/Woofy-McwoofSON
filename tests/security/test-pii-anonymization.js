// 🦴 Test: PII Anonymization

const assert = require('assert');
const anonymize = require('../../src/security/anonymize');

describe('PII Anonymization', () => {
  it('should remove names and emails from text', () => {
    const input = "Name: Jane Doe, Email: jane@example.com";
    const output = anonymize(input);
    assert(!output.includes("Jane"));
    assert(!output.includes("jane@example.com"));
  });
});