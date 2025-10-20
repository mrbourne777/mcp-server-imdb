"""
Example usage of the FM-DB MCP Server

This script demonstrates how to use the MCP server tools programmatically.
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from fm_db_server.server import search_movies, get_movie_poster, get_movie_trailer


async def example_movie_search():
    """Example: Search for movies by title"""
    print("=" * 60)
    print("Example 1: Searching for 'Inception'")
    print("=" * 60)
    
    result = await search_movies(q="Inception")
    
    if result.get("ok"):
        movies = result.get("description", [])
        print(f"\nFound {len(movies)} results:")
        for i, movie in enumerate(movies[:3], 1):  # Show first 3 results
            print(f"\n{i}. {movie.get('#TITLE')} ({movie.get('#YEAR', 'N/A')})")
            print(f"   IMDb ID: {movie.get('#IMDB_ID')}")
            print(f"   Rating Rank: {movie.get('#RANK', 'N/A')}")
            print(f"   Actors: {movie.get('#ACTORS', 'N/A')}")
    else:
        print(f"Error: {result}")


async def example_movie_details():
    """Example: Get detailed information about a specific movie"""
    print("\n" + "=" * 60)
    print("Example 2: Getting details for 'The Dark Knight' (tt0468569)")
    print("=" * 60)
    
    result = await search_movies(tt="tt0468569")
    
    if result.get("ok"):
        movie = result.get("short", {})
        print(f"\nTitle: {movie.get('name')}")
        print(f"Release Date: {movie.get('datePublished')}")
        print(f"Rating: {movie.get('aggregateRating', {}).get('ratingValue')}/10")
        print(f"Votes: {movie.get('aggregateRating', {}).get('ratingCount')}")
        print(f"Genre: {', '.join(movie.get('genre', []))}")
        print(f"\nDescription: {movie.get('description')}")
    else:
        print(f"Error: {result}")


async def example_tv_series_season():
    """Example: Get episodes from a TV series season"""
    print("\n" + "=" * 60)
    print("Example 3: Getting Breaking Bad Season 1 episodes (tt0959621)")
    print("=" * 60)
    
    result = await search_movies(tt="tt0959621", lsn=1)
    
    if result.get("ok"):
        print("\nTV Series season episodes retrieved successfully!")
        # The API structure for season data may vary
        print(f"Result keys: {list(result.keys())}")
    else:
        print(f"Error: {result}")


async def example_poster_and_trailer():
    """Example: Get poster and trailer for a movie"""
    print("\n" + "=" * 60)
    print("Example 4: Getting poster and trailer for 'Interstellar' (tt0816692)")
    print("=" * 60)
    
    # Note: These endpoints may return empty responses depending on API availability
    poster_result = await get_movie_poster("tt0816692")
    print(f"\nPoster result: {poster_result}")
    
    trailer_result = await get_movie_trailer("tt0816692")
    print(f"\nTrailer result: {trailer_result}")


async def main():
    """Run all examples"""
    await example_movie_search()
    await example_movie_details()
    await example_tv_series_season()
    await example_poster_and_trailer()
    
    print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
