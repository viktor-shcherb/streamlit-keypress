(() => {
    const pressedKeys = [];

    // Add event listener to capture keyboard events
    window.parent.document.addEventListener('keydown', function (e) {
        console.log('Key pressed:', e.key);
        pressedKeys.push(e.key);
    });

    // Return queued keys on each render and clear the queue
    Streamlit.onRender(() => {
        Streamlit.setComponentValue(pressedKeys);
        pressedKeys.length = 0;
    });

    // Initialize component
    Streamlit.setComponentReady();
})();
