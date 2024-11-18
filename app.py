import streamlit as st
import json
import datetime
import os
import glob

def get_json_files():
    # Get all JSON files from workspaceStorage directory
    json_files = glob.glob('workspaceStorage/*.json')
    # Return just the filenames without path
    return [os.path.basename(f) for f in json_files]

def load_chat_data(json_file):
    # Prepend the directory path
    full_path = os.path.join('workspaceStorage', json_file)
    with open(full_path, 'r') as f:
        data = json.load(f)
    
    # Extract chat data from the JSON
    chat_data = json.loads(data['rows'][1][2])  # Get the chat data from second row
    return chat_data

def format_time_ago(timestamp_ms):
    now = datetime.datetime.now()
    timestamp = datetime.datetime.fromtimestamp(timestamp_ms / 1000)  # Convert ms to seconds
    diff = now - timestamp
    
    if diff.days > 0:
        return f"{diff.days}d ago"
    elif diff.seconds // 3600 > 0:
        return f"{diff.seconds // 3600}h ago"
    else:
        return f"{diff.seconds // 60}m ago"

def display_chat_message(message):
    # Determine message style based on type
    is_user = message.get('type') == 'user'
    
    # Create columns for avatar and message
    col1, col2 = st.columns([1, 11])
    
    with col1:
        # Display avatar
        if is_user:
            st.write("👤")  # User avatar
        else:
            st.write("🤖")  # AI avatar
    
    with col2:
        # Create message container
        container = st.container()
        with container:
            # Display message content
            if 'text' in message:
                st.markdown(message['text'])

def main():
    st.set_page_config(layout="wide")
    
    # Sidebar
    with st.sidebar:
        st.title("Cursor History 🕒")
        
        # Add session selector
        json_files = get_json_files()
        selected_session = st.selectbox(
            "Session",
            json_files,
            index=0 if json_files else None
        )
        
        st.subheader("All Chats")
        st.text_input("Search chats...", placeholder="Search chats...")
        
        if selected_session:
            # Load chat data for selected session
            chat_data = load_chat_data(selected_session)
            
            # Display chat list
            for tab in chat_data['tabs']:
                chat_title = tab['chatTitle']
                # Get last message timestamp if available
                last_time = tab.get('lastSendTime', 0)
                time_ago = format_time_ago(last_time) if last_time else ""
                
                if st.button(f"{chat_title}\n{time_ago}", key=tab['tabId']):
                    st.session_state.selected_chat = tab
    
    # Main chat display
    if 'selected_chat' in st.session_state:
        selected_chat = st.session_state.selected_chat
        st.subheader(selected_chat['chatTitle'])
        
        # Display chat messages
        for bubble in selected_chat['bubbles']:
            display_chat_message(bubble)

if __name__ == "__main__":
    main() 