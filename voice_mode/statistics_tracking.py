"""Statistics tracking functions used by voice tools.

This module contains tracking functions that can be imported by tools
without causing the statistics tools themselves to be loaded.
"""

from typing import Optional
from .statistics import track_conversation
from .config import logger


def track_voice_interaction(message: str, 
                           response: str,
                           timing_str: Optional[str] = None,
                           transport: Optional[str] = None,
                           voice_provider: Optional[str] = None,
                           voice_name: Optional[str] = None,
                           model: Optional[str] = None,
                           success: bool = True,
                           error_message: Optional[str] = None) -> None:
    """
    Track a voice interaction for statistics.
    
    This function should be called from conversation tools to record metrics.
    """
    try:
        track_conversation(
            message=message,
            response=response,
            timing_str=timing_str,
            transport=transport,
            voice_provider=voice_provider,
            voice_name=voice_name,
            model=model,
            success=success,
            error_message=error_message
        )
        logger.debug(f"Tracked voice interaction: {len(message)} chars, success={success}")
        
    except Exception as e:
        logger.error(f"Error tracking voice interaction: {e}")
        # Don't raise the error - statistics tracking shouldn't break the main flow