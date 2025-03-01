import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image
import io

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def analyze_with_gemini(image_file):
    """Analyzes a medical image and returns structured AI-generated results."""
    try:
        image = Image.open(image_file).convert("RGB")

        prompt = (
            "Analyze this medical image for possible cancer indicators. "
            "Ensure that you provide a structured response in this exact format: "
            "\n\n🔍 Findings: [Briefly describe the lesion, including size, shape, location, and characteristics.]"
            "\n⚠️ Concerns: [Highlight any abnormalities such as irregular borders, rapid growth, necrosis, or other warning signs.]"
            "\n🎯 Cancer Probability: [Give a percentage range (e.g., 60-80%) based on visual patterns of malignancy.]"
            "\n🧬 Possible Cancer Type: [Specify the most likely type of cancer, such as glioblastoma, lymphoma, oral squamous cell carcinoma, etc.]"
            "\nEnsure each section is present in the response. If no clear cancerous signs are detected, return 'Low probability (<10%)'."
        )

        response = model.generate_content([prompt, image])

        if response and hasattr(response, "parts") and response.parts:
            text_response = response.parts[0].text.strip()

            disclaimer_start = text_response.find("**Disclaimer:**")
            if disclaimer_start != -1:
                text_response = text_response[:disclaimer_start].strip()

            print("🔹 DEBUG: Cleaned AI Response:\n", text_response)

        else:
            return {"error": "AI model did not return a response."}

        return {
            "findings": extract_section(text_response, "🔍 Findings:"),
            "concerns": extract_section(text_response, "⚠️ Concerns:"),
            "probability": extract_section(text_response, "🎯 Cancer Probability:"),
            "cancer_type": extract_section(text_response, "🧬 Possible Cancer Type:"),
        }

    except Exception as e:
        print("Error processing image:", e)
        return {"error": f"Error processing image: {str(e)}"}

def extract_section(text, section_title):
    """Extracts a specific section from the AI response text."""
    try:
        start = text.find(section_title)
        if start == -1:
            return "Not available"
        end = text.find("\n", start + len(section_title))
        if end == -1:
            return text[start + len(section_title):].strip()
        return text[start + len(section_title):end].strip()
    except Exception as e:
        return f"Error extracting section: {str(e)}"
