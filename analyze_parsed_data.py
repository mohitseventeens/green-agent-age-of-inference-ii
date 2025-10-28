import json
from pathlib import Path
from collections import Counter
import pandas as pd

# This script assumes it is run from the project's root directory.
PROFILES_DIR = Path("data/profiles")
PARSED_JOBS_FILE = Path("data/parsed_jobs.json")
PARSED_TRAININGS_FILE = Path("data/parsed_trainings.json")

def analyze_persona_profiles():
    """Analyzes the distribution of attributes across all persona profiles."""
    print("\n--- 📊 Analyzing Persona Profiles ---")
    
    if not PROFILES_DIR.exists():
        print(f"❌ ERROR: Profiles directory not found at '{PROFILES_DIR}'")
        return

    all_profiles = []
    for profile_file in PROFILES_DIR.glob("*.json"):
        with open(profile_file, 'r') as f:
            all_profiles.append(json.load(f))
            
    if not all_profiles:
        print("No persona profiles found to analyze.")
        return

    df = pd.DataFrame(all_profiles)
    
    print(f"\nTotal Personas Analyzed: {len(df)}")

    # 1. Education Level Distribution
    print("\n🎓 Education Level Distribution:")
    edu_counts = df['education_level'].value_counts().sort_index()
    print(edu_counts.to_string())

    # 2. Experience Distribution
    print("\n📈 Years of Experience Distribution:")
    exp_counts = df['experience_years'].value_counts().sort_index()
    print(exp_counts.to_string())
    print(f"  - Average Experience: {df['experience_years'].mean():.2f} years")
    print(f"  - Median Experience: {df['experience_years'].median():.2f} years")

    # 3. Location Distribution
    print("\n📍 Location Distribution (Top 5):")
    loc_counts = df['city'].value_counts()
    print(loc_counts.head(5).to_string())


def analyze_parsed_file(file_path: Path, item_type: str):
    """Generic analyzer for parsed jobs or trainings JSON files."""
    print(f"\n--- 📊 Analyzing Parsed {item_type.capitalize()} Data ---")
    
    if not file_path.exists():
        print(f"❌ ERROR: Parsed data file not found at '{file_path}'")
        return
        
    with open(file_path, 'r') as f:
        data = json.load(f)
    
    df = pd.DataFrame(data)
    print(f"\nTotal {item_type.capitalize()} Analyzed: {len(df)}")
    
    if item_type == "jobs":
        # 1. Education Requirements
        print("\n🎓 Required Education Level Distribution:")
        edu_counts = df['education_level'].fillna('Not Specified').value_counts().sort_index()
        print(edu_counts.to_string())

        # 2. Experience Requirements
        print("\n📈 Required Years of Experience Distribution:")
        exp_counts = df['experience_years'].value_counts().sort_index()
        print(exp_counts.to_string())

        # 3. Location Distribution
        print("\n📍 Location Distribution (Top 5):")
        loc_counts = df['city'].fillna('Not Specified').value_counts()
        print(loc_counts.head(5).to_string())
        print(f"  - Remote Jobs: {df['is_remote'].sum()}")

    elif item_type == "trainings":
        # 1. Training Prerequisites
        print("\n🎓 Required Prerequisite Level Distribution:")
        req_counts = df['required_level'].fillna('Not Specified').value_counts().sort_index()
        print(req_counts.to_string())


if __name__ == "__main__":
    print("--- 🔬 Kicking off Data-Driven Filter Analysis ---")
    analyze_persona_profiles()
    analyze_parsed_file(PARSED_JOBS_FILE, "jobs")
    analyze_parsed_file(PARSED_TRAININGS_FILE, "trainings")
    print("\n--- ✅ Analysis Complete ---")