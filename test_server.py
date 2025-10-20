"""
Test script to verify the FM-DB MCP Server tools
"""

import asyncio
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from fm_db_server.server import search_movies, get_movie_poster, get_movie_trailer


async def test_tools():
    """Test all the MCP server tools"""
    
    print("=" * 60)
    print("Testing FM-DB MCP Server Tools")
    print("=" * 60)
    
    # Test 1: Search for a movie by title
    print("\n1. Testing search_movies with query 'The Matrix'...")
    result1 = await search_movies(q="The Matrix")
    print(f"Result: {result1}")
    
    # Test 2: Get movie details by IMDb ID
    print("\n2. Testing search_movies with IMDb ID 'tt0133093' (The Matrix)...")
    result2 = await search_movies(tt="tt0133093")
    print(f"Result: {result2}")
    
    # Test 3: Get poster
    print("\n3. Testing get_movie_poster for 'tt0133093' (The Matrix)...")
    result3 = await get_movie_poster(imdb_id="tt0133093")
    print(f"Result: {result3}")
    
    # Test 4: Get trailer
    print("\n4. Testing get_movie_trailer for 'tt0133093' (The Matrix)...")
    result4 = await get_movie_trailer(imdb_id="tt0133093")
    print(f"Result: {result4}")
    
    # Test 5: Search with no parameters (should return error)
    print("\n5. Testing search_movies with no parameters (should error)...")
    result5 = await search_movies()
    print(f"Result: {result5}")
    
    print("\n" + "=" * 60)
    print("All tests completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(test_tools())
