"""
FM-DB MCP Server - Free Movie Database API Integration

This MCP server provides tools to interact with the FM-DB API (Free Movie Database),
allowing you to search for movies on IMDb, retrieve poster images, and get trailer videos.

Tools:
- search_movies: Search for movies on IMDb by query or IMDb ID
- get_movie_poster: Get the poster photo URL for an IMDb ID
- get_movie_trailer: Get the trailer video URL for an IMDb ID
"""

from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("fm-db-api")

# Constants
FM_DB_API_BASE = "https://imdb.iamidiotareyoutoo.com"
USER_AGENT = "mcp-fm-db-server/1.0"


async def make_api_request(endpoint: str, params: dict[str, Any] | None = None) -> dict[str, Any]:
    """Make an HTTP request to the FM-DB API."""
    async with httpx.AsyncClient() as client:
        headers = {"User-Agent": USER_AGENT}
        response = await client.get(
            f"{FM_DB_API_BASE}{endpoint}",
            params=params,
            headers=headers,
            timeout=30.0
        )
        response.raise_for_status()
        return response.json()


@mcp.tool()
async def search_movies(
    q: str = "",
    tt: str = "",
    lsn: int = 0
) -> dict[str, Any]:
    """
    Search for movies on IMDb or get detailed information about a specific title.
    
    At least one of 'q' or 'tt' must be provided.
    
    Args:
        q: Search query - a word or phrase to search for (e.g., "The Matrix", "Christopher Nolan")
        tt: IMDb ID to get detailed information (e.g., "tt0133093" for The Matrix)
        lsn: Season number - if the IMDb ID is a TV series, fetch episodes for this season
    
    Returns:
        Search results containing movie/TV show information including titles, years, ratings, cast, etc.
    
    Examples:
        - search_movies(q="The Dark Knight")
        - search_movies(tt="tt0468569")
        - search_movies(tt="tt0944947", lsn=1)  # Game of Thrones Season 1
    """
    if not q and not tt:
        return {
            "error": "At least one of 'q' (search query) or 'tt' (IMDb ID) must be provided"
        }
    
    params = {}
    if q:
        params["q"] = q
    if tt:
        params["tt"] = tt
    if lsn is not None:
        params["lsn"] = lsn
    
    try:
        result = await make_api_request("/search", params)
        return result
    except httpx.HTTPStatusError as e:
        return {
            "error": f"API request failed with status {e.response.status_code}",
            "details": str(e)
        }
    except Exception as e:
        return {
            "error": f"Request failed: {str(e)}"
        }


@mcp.tool()
async def get_movie_poster(imdb_id: str) -> dict[str, Any]:
    """
    Get the poster photo URL for a movie or TV show by its IMDb ID.
    
    Args:
        imdb_id: The IMDb ID (e.g., "tt0133093" for The Matrix)
    
    Returns:
        Dictionary containing the poster image URL and metadata
    
    Example:
        get_movie_poster(imdb_id="tt0133093")
    """
    if not imdb_id:
        return {"error": "IMDb ID is required"}
    
    # Remove 'tt' prefix if included, as the endpoint expects just the ID
    clean_id = imdb_id.replace("tt", "") if imdb_id.startswith("tt") else imdb_id
    
    try:
        result = await make_api_request(f"/photo/{clean_id}")
        return result
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return {
                "error": f"No poster found for IMDb ID: {imdb_id}",
                "details": "The movie/show may not have a poster available"
            }
        return {
            "error": f"API request failed with status {e.response.status_code}",
            "details": str(e)
        }
    except Exception as e:
        return {
            "error": f"Request failed: {str(e)}"
        }


@mcp.tool()
async def get_movie_trailer(imdb_id: str) -> dict[str, Any]:
    """
    Get the trailer video URL for a movie or TV show by its IMDb ID.
    
    Args:
        imdb_id: The IMDb ID (e.g., "tt0133093" for The Matrix)
    
    Returns:
        Dictionary containing the trailer video URL and metadata
    
    Example:
        get_movie_trailer(imdb_id="tt0133093")
    """
    if not imdb_id:
        return {"error": "IMDb ID is required"}
    
    # Remove 'tt' prefix if included, as the endpoint expects just the ID
    clean_id = imdb_id.replace("tt", "") if imdb_id.startswith("tt") else imdb_id
    
    try:
        result = await make_api_request(f"/media/{clean_id}")
        return result
    except httpx.HTTPStatusError as e:
        if e.response.status_code == 404:
            return {
                "error": f"No trailer found for IMDb ID: {imdb_id}",
                "details": "The movie/show may not have a trailer available"
            }
        return {
            "error": f"API request failed with status {e.response.status_code}",
            "details": str(e)
        }
    except Exception as e:
        return {
            "error": f"Request failed: {str(e)}"
        }


if __name__ == "__main__":
    # Run the MCP server
    mcp.run()

