import React from 'react';

const StopIcon = ({ icon, title, description, active }) => {
  return (
    <div className={`stop-icon ${active ? 'active' : ''}`}>
      <img src={icon} alt={title} />
      {active && (
        <div className="popup">
          <h3>{title}</h3>
          <p>{description}</p>
        </div>
      )}
    </div>
  );
}

export default StopIcon;