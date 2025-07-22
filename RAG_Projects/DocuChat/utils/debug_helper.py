# utils/debug_helper.py
import os
import tempfile

def debug_file_info(uploaded_file):
    """Debug function to inspect uploaded file details"""
    info = {
        'name': uploaded_file.name if hasattr(uploaded_file, 'name') else 'No name attribute',
        'size': uploaded_file.size if hasattr(uploaded_file, 'size') else 'No size attribute',
        'type': uploaded_file.type if hasattr(uploaded_file, 'type') else 'No type attribute',
    }
    
    # Try to get file extension
    try:
        if uploaded_file.name:
            name_parts = uploaded_file.name.split('.')
            info['extension'] = name_parts[-1].lower() if len(name_parts) > 1 else 'No extension'
            info['name_parts_count'] = len(name_parts)
        else:
            info['extension'] = 'No name to extract extension from'
    except Exception as e:
        info['extension_error'] = str(e)
    
    return info

# Add this to your app.py for debugging:
# if uploaded_files:
#     for file in uploaded_files:
#         st.write("Debug info:", debug_file_info(file))
