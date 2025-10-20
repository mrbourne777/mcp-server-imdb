# FM-DB MCP Server

A Model Context Protocol (MCP) server that integrates with the FM-DB API (Free Movie Database) to provide movie and TV show information from IMDb.

## Features

This MCP server provides three tools for interacting with the FM-DB API:

### 🔍 search_movies
Search for movies and TV shows on IMDb or get detailed information about a specific title.

**Parameters:**
- `q` (optional): Search query - a word or phrase to search for
- `tt` (optional): IMDb ID to get detailed information
- `lsn` (optional): Season number - if the IMDb ID is a TV series, fetch episodes for this season

**Note:** At least one of `q` or `tt` must be provided.

**Examples:**
```python
# Search by title
search_movies(q="The Dark Knight")

# Get details by IMDb ID
search_movies(tt="tt0468569")

# Get TV series season episodes
search_movies(tt="tt0944947", lsn=1)  # Game of Thrones Season 1
```

### 🖼️ get_movie_poster
Get the poster photo URL for a movie or TV show.

**Parameters:**
- `imdb_id`: The IMDb ID (e.g., "tt0133093" for The Matrix)

**Example:**
```python
get_movie_poster(imdb_id="tt0133093")
```

### 🎬 get_movie_trailer
Get the trailer video URL for a movie or TV show.

**Parameters:**
- `imdb_id`: The IMDb ID (e.g., "tt0133093" for The Matrix)

**Example:**
```python
get_movie_trailer(imdb_id="tt0133093")
```

## Installation

1. Ensure you have Python 3.12 or higher installed
2. Install dependencies:

```bash
uv pip install -e .
```

## Usage

### Running the Server

To run the server using FastMCP:

```bash
# Using uv (recommended)
uv run run_server.py

# Or run directly
python3 run_server.py
```

### Testing the Server

You can test the server functionality with the included test script:

```bash
uv run test_server.py
```

### Connecting to MCP Clients

#### Claude Desktop

Add this to your `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "fm-db": {
      "command": "uv",
      "args": [
        "--directory",
        "/path/to/mcp-server",
        "run",
        "run_server.py"
      ]
    }
  }
}
```

Replace `/path/to/mcp-server` with the actual path to this directory.

#### Other MCP Clients

This server uses the standard MCP protocol and can be connected to any MCP-compatible client that supports STDIO transport.

## API Information

This server uses the FM-DB API (Free Movie Database):
- **Base URL:** https://imdb.iamidiotareyoutoo.com
- **Documentation:** https://imdb.iamidiotareyoutoo.com/docs/index.html
- **License:** GNU Affero General Public License 3.0

All content and images are contributed and maintained by FM-DB users. No API keys are required.

## Development

### Project Structure

```
mcp-server/
├── main.py              # MCP server implementation
├── pyproject.toml       # Project dependencies
└── README.md           # This file
```

### Dependencies

- `mcp>=1.17.0` - Model Context Protocol SDK
- `httpx>=0.27.0` - HTTP client for API requests

## Example Use Cases

1. **Movie Search:** Find movies by title, actor, director, or keywords
2. **Detailed Information:** Get comprehensive details about a specific movie or TV show
3. **TV Series Episodes:** Fetch episode lists for specific seasons
4. **Visual Assets:** Retrieve poster images for movies and shows
5. **Trailers:** Access trailer videos for promotional content

## License

This project follows the licensing of the FM-DB API (GNU Affero General Public License 3.0).

## Support

For issues or feature requests:
- FM-DB API: https://github.com/TelegramPlayGround/Unofficial-IMDb-API/issues
- MCP Protocol: https://modelcontextprotocol.io
