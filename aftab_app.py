from flask import Flask, request, send_file
import gdspy
import matplotlib.pyplot as plt

app = Flask(__name__)

@app.route('/render-gds', methods=['GET'])
def render_gds():
    try:
        # Load the GDS file
        gdsii = gdspy.GdsLibrary()
        gdsii.read_gds('18.gds')

        # Get the top cell
        top_cell = gdsii.top_level()[0]

        # Create a figure
        fig, ax = plt.subplots()
        for polygon in top_cell.get_polygons():
            for p in polygon:
                x, y = zip(*p)
                ax.fill(x, y, 'black', alpha=0.5)

        # Remove axes
        ax.set_aspect('equal')
        ax.axis('off')

        # Save the image
        image_path = "static/gds_render.png"
        plt.savefig(image_path, dpi=300, bbox_inches='tight')
        plt.close()

        return send_file(image_path, mimetype='image/png')

    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True)
