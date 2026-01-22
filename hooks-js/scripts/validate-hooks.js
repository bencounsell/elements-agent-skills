#!/usr/bin/env node

/**
 * Simple validation script for Elements hooks.js files
 * Usage: node validate-hooks.js path/to/hooks.js
 */

const fs = require('fs');
const path = require('path');

function validateHooksFile(filePath) {
  const errors = [];
  const warnings = [];

  // Check file exists
  if (!fs.existsSync(filePath)) {
    console.error(`Error: File not found: ${filePath}`);
    process.exit(1);
  }

  const content = fs.readFileSync(filePath, 'utf8');

  // Check for transformHook function
  if (!content.includes('transformHook')) {
    errors.push('Missing transformHook function');
  }

  // Check for exports
  if (!content.includes('exports.transformHook')) {
    errors.push('Missing exports.transformHook = transformHook');
  }

  // Check for rw parameter
  if (content.includes('transformHook') && !content.includes('(rw)')) {
    warnings.push('transformHook should accept (rw) parameter');
  }

  // Check for common mistakes
  if (content.includes('rw.props.') && content.includes('rw.setProps')) {
    // Good pattern
  }

  if (content.includes('module.exports')) {
    warnings.push('Use exports.transformHook instead of module.exports');
  }

  // Check for async (not supported)
  if (content.includes('async') || content.includes('await')) {
    errors.push('Async/await is not supported in hooks.js');
  }

  // Output results
  console.log(`\nValidating: ${filePath}\n`);

  if (errors.length === 0 && warnings.length === 0) {
    console.log('✅ No issues found');
  } else {
    if (errors.length > 0) {
      console.log('Errors:');
      errors.forEach(e => console.log(`  ❌ ${e}`));
    }
    if (warnings.length > 0) {
      console.log('Warnings:');
      warnings.forEach(w => console.log(`  ⚠️  ${w}`));
    }
  }

  process.exit(errors.length > 0 ? 1 : 0);
}

// Run validation
const filePath = process.argv[2];
if (!filePath) {
  console.log('Usage: node validate-hooks.js path/to/hooks.js');
  process.exit(1);
}

validateHooksFile(filePath);
