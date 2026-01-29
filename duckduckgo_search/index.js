const { exec } = require('child_process');
const path = require('path');

/**
 * DuckDuckGo Search Skill for Clawdbot
 * 
 * This skill allows Clawdbot to perform web searches using DuckDuckGo 
 * without requiring an API key by calling the Python ddgs library.
 */

/**
 * Performs a DuckDuckGo search with the given query
 * @param {string} query - The search query string
 * @param {number} num_results - Number of results to return (default: 5)
 * @returns {Promise<Array>} - Promise that resolves to search results array
 */
async function search(query, num_results = 5) {
    return new Promise((resolve, reject) => {
        // Get the absolute path to the Python script
        const scriptPath = path.join(__dirname, 'ddg_search_json.py');
        
        // Build the command
        const command = `python3 "${scriptPath}" "${query}" -n ${num_results}`;
        
        // Execute the Python script
        exec(command, { timeout: 10000 }, (error, stdout, stderr) => {
            if (error) {
                console.error('DuckDuckGo search error:', error);
                console.error('stderr:', stderr);
                reject(new Error(`Search failed: ${error.message}`));
                return;
            }
            
            if (stderr) {
                console.warn('DuckDuckGo search stderr:', stderr);
            }
            
            try {
                // Parse the JSON output from Python script
                const results = JSON.parse(stdout.trim());
                resolve(results);
            } catch (parseError) {
                console.error('Failed to parse JSON output:', stdout);
                reject(new Error(`Failed to parse search results: ${parseError.message}`));
            }
        });
    });
}

module.exports = { search };