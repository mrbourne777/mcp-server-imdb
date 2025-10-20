# FM-DB MCP Server - Quick Start Guide

## What is this?

This is a Model Context Protocol (MCP) server that provides access to the FM-DB (Free Movie Database) API. It allows AI assistants like Claude to search for movies, get movie details, and access poster images and trailers directly from IMDb data.

## Quick Setup

1. **Install dependencies:**
   ```bash
   uv pip install -e .
   ```

2. **Test the server:**
   ```bash
   uv run test_server.py
   ```

3. **Run the server:**
   ```bash
   uv run run_server.py
   ```

## Available Tools

### 1. search_movies
Search for movies or get detailed information about specific titles.

**Parameters:**
- `q` (optional): Search query string
- `tt` (optional): IMDb ID (e.g., "tt0133093")
- `lsn` (optional): Season number for TV series

**Examples:**
```python
# Search by title
search_movies(q="The Matrix")

# Get details by IMDb ID
search_movies(tt="tt0133093")

# Get TV series season
search_movies(tt="tt0944947", lsn=1)
```

### 2. get_movie_poster
Get the poster image URL for a movie.

**Parameters:**
- `imdb_id`: The IMDb ID

**Example:**
```python
get_movie_poster(imdb_id="tt0133093")
```

### 3. get_movie_trailer
Get the trailer video URL for a movie.

**Parameters:**
- `imdb_id`: The IMDb ID

**Example:**
```python
get_movie_trailer(imdb_id="tt0133093")
```

## Integration with Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "fm-db": {
      "command": "uv",
      "args": [
        "--directory",
        "/absolute/path/to/mcp-server",
        "run",
        "run_server.py"
      ]
    }
  }
}
```

## Example Queries for Claude

Once connected to Claude Desktop, you can ask:

- "Search for movies directed by Christopher Nolan"
- "Tell me about the movie The Matrix using its IMDb ID tt0133093"
- "Find the top-rated action movies from 1999"
- "Get me the poster for Inception"
- "Show me episodes from Breaking Bad season 1"

## Project Structure

```
mcp-server/
├── src/
│   └── fm_db_server/
│       ├── __init__.py
│       └── server.py          # Main server implementation
├── run_server.py              # Entry point to run the server
├── test_server.py             # Test script
├── examples.py                # Usage examples
├── pyproject.toml             # Project configuration
└── README.md                  # Full documentation
```

## API Information

- **API Base URL:** https://imdb.iamidiotareyoutoo.com
- **Documentation:** https://imdb.iamidiotareyoutoo.com/docs/index.html
- **License:** GNU Affero General Public License 3.0
- **No API key required**

## Troubleshooting

**Import errors when running:**
Make sure you've installed the package:
```bash
uv pip install -e .
```

**Server not connecting in Claude:**
- Verify the path in `claude_desktop_config.json` is absolute
- Check that `uv` is in your PATH
- Restart Claude Desktop after configuration changes

**Empty results from poster/trailer endpoints:**
This is expected - not all movies have posters or trailers available in the API.

## Development

Run the examples to see the server in action:
```bash
uv run examples.py
```

This will demonstrate all three tools with real movie data.

## Support

- Report issues at the FM-DB API repository
- MCP Protocol documentation: https://modelcontextprotocol.io
