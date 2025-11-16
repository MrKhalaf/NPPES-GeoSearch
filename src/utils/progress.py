"""Terminal progress bar utilities."""

import sys
from typing import Optional


class ProgressBar:
    """Simple terminal progress bar."""
    
    def __init__(self, total: int, width: int = 40, desc: str = "Progress"):
        """Initialize progress bar.
        
        Args:
            total: Total number of steps
            width: Width of progress bar in characters
            desc: Description text
        """
        self.total = total
        self.width = width
        self.desc = desc
        self.current = 0
        self._last_length = 0
    
    def update(self, n: int = 1, status: Optional[str] = None):
        """Update progress by n steps.
        
        Args:
            n: Number of steps to advance
            status: Optional status message
        """
        self.current = min(self.current + n, self.total)
        self._display(status)
    
    def set(self, value: int, status: Optional[str] = None):
        """Set progress to specific value.
        
        Args:
            value: Progress value (0 to total)
            status: Optional status message
        """
        self.current = max(0, min(value, self.total))
        self._display(status)
    
    def _display(self, status: Optional[str] = None):
        """Display the progress bar."""
        if self.total == 0:
            percent = 100
        else:
            percent = int(100 * self.current / self.total)
        
        filled = int(self.width * self.current / self.total) if self.total > 0 else self.width
        bar = "█" * filled + "░" * (self.width - filled)
        
        status_text = f" | {status}" if status else ""
        text = f"\r{self.desc}: [{bar}] {percent}% ({self.current}/{self.total}){status_text}"
        
        # Clear previous line if needed
        sys.stdout.write(" " * self._last_length + "\r")
        sys.stdout.write(text)
        sys.stdout.flush()
        
        self._last_length = len(text)
    
    def finish(self, message: Optional[str] = None):
        """Finish the progress bar.
        
        Args:
            message: Optional completion message
        """
        self.set(self.total, message)
        sys.stdout.write("\n")
        sys.stdout.flush()
        self._last_length = 0


def print_step(step: str, detail: Optional[str] = None):
    """Print a step message.
    
    Args:
        step: Step description
        detail: Optional detail message
    """
    detail_text = f" - {detail}" if detail else ""
    print(f"→ {step}{detail_text}")

