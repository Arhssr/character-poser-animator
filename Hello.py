import streamlit as st
import numpy as np
import cv2


# Create a Streamlit app
st.title("2D Character Animator and Poser")

# Upload character image
character_image = st.file_uploader("Upload Character Image (PNG or JPG)", type=["png", "jpg", "jpeg"])

if character_image:
    # Display the uploaded character image
    st.image(character_image, caption="Uploaded Character Image", use_column_width=True)

    # Create sliders for limb positions
    st.subheader("Character Limb Poser")
    left_arm_x = st.slider("Left Arm X", min_value=-50, max_value=50, value=0)
    left_arm_y = st.slider("Left Arm Y", min_value=-50, max_value=50, value=0)
    right_arm_x = st.slider("Right Arm X", min_value=-50, max_value=50, value=0)
    right_arm_y = st.slider("Right Arm Y", min_value=-50, max_value=50, value=0)

    # Process and display the character with adjusted limb positions
    if st.button("Apply Pose"):
        if character_image:
            character = cv2.imread(character_image.name)
            character = cv2.cvtColor(character, cv2.COLOR_BGR2RGB)

            # Apply limb adjustments (this is a simplified example)
            # Adjust the pixel coordinates based on sliders
            character_height, character_width, _ = character.shape
            left_arm_x = character_width // 2 + left_arm_x
            left_arm_y = character_height // 2 + left_arm_y
            right_arm_x = character_width // 2 + right_arm_x
            right_arm_y = character_height // 2 + right_arm_y

            # Draw limbs on the character image (simplified)
            cv2.line(character, (character_width // 2, character_height // 2),
                     (left_arm_x, left_arm_y), (0, 255, 0), 5)
            cv2.line(character, (character_width // 2, character_height // 2),
                     (right_arm_x, right_arm_y), (0, 255, 0), 5)

            # Display the character with adjusted limbs
            st.image(character, caption="Character with Pose", use_column_width=True)
import streamlit as st
import numpy as np
import cv2


# Create a Streamlit app
st.title("2D Character Animator and Poser")

# Upload character image
character_image = st.file_uploader("Upload Character Image (PNG or JPG)", type=["png", "jpg", "jpeg"])

if character_image:
    # Display the uploaded character image
    st.image(character_image, caption="Uploaded Character Image", use_column_width=True)

    # Create sliders for limb positions
    st.subheader("Character Limb Poser")
    left_arm_x = st.slider("Left Arm X", min_value=-50, max_value=50, value=0)
    left_arm_y = st.slider("Left Arm Y", min_value=-50, max_value=50, value=0)
    right_arm_x = st.slider("Right Arm X", min_value=-50, max_value=50, value=0)
    right_arm_y = st.slider("Right Arm Y", min_value=-50, max_value=50, value=0)

    # Process and display the character with adjusted limb positions
    if st.button("Apply Pose"):
        if character_image:
            character = cv2.imread(character_image.name)
            character = cv2.cvtColor(character, cv2.COLOR_BGR2RGB)

            # Apply limb adjustments (this is a simplified example)
            # Adjust the pixel coordinates based on sliders
            character_height, character_width, _ = character.shape
            left_arm_x = character_width // 2 + left_arm_x
            left_arm_y = character_height // 2 + left_arm_y
            right_arm_x = character_width // 2 + right_arm_x
            right_arm_y = character_height // 2 + right_arm_y

            # Draw limbs on the character image (simplified)
            cv2.line(character, (character_width // 2, character_height // 2),
                     (left_arm_x, left_arm_y), (0, 255, 0), 5)
            cv2.line(character, (character_width // 2, character_height // 2),
                     (right_arm_x, right_arm_y), (0, 255, 0), 5)

            # Display the character with adjusted limbs
            st.image(character, caption="Character with Pose", use_column_width=True)
