# 1. Change the version comment near the top (line 13):
#    FROM: # Version: 1.0.1
#    TO:
# Version: 2.0 - Automated Deployment

# 2. Add this route anywhere with your other routes (e.g. after the index route):

@app.route('/health')
def health():
    """Health check endpoint for automated deployment verification"""
    from datetime import datetime
    return jsonify({
        'status': 'healthy',
        'version': '2.0',
        'deployment_method': 'automated',
        'assignment': 'Automated EC2 Deployment',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/version')
def version():
    """Version page to prove automated pipeline ran"""
    from datetime import datetime
    return f'''
    <h1>Audio Error Labeling Tool</h1>
    <p><strong>Version:</strong> 2.0 - Automated Deployment</p>
    <p><strong>Deployed via:</strong> GitHub Actions + AWS SSM</p>
    <p><strong>Build Date:</strong> {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>
    <p><strong>Assignment:</strong> Automated EC2 Deployment</p>
    <p><a href="/">Go to main app</a></p>
    '''
