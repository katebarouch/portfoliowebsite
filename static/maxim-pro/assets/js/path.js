import React, { useState, useEffect } from 'react';
import StopIcon from '../StopIcon';

const Path = () => {
  const [activeStop, setActiveStop] = useState(0);

  useEffect(() => {
    const handleKeyPress = (event) => {
      if (event.key === "ArrowUp" && activeStop > 0) {
        setActiveStop(prevStop => prevStop - 1);
      } else if (event.key === "ArrowDown" && activeStop < stops.length - 1) {
        setActiveStop(prevStop => prevStop + 1);
      }
    };

    window.addEventListener('keydown', handleKeyPress);

    return () => window.removeEventListener('keydown', handleKeyPress);
  }, [activeStop]);

  return (
    <div className="path">
      {stops.map((stop, index) => (
        <StopIcon key={index} active={index === activeStop} {...stop} />
      ))}
    </div>
  );
}

export default Path;