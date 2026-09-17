import streamlit as st
import json
from gemini_helpers import slugify, normalize_phone, build_schema

st.set_page_config(page_title="RankAI - WNY Restoration", layout="wide", page_icon="🏗️")

st.title("🏗️ RankAI: Restoration & Contracting SEO Engine")
st.caption("Marketing Command Center for WNY Restoration General Contracting LLC")

# Sidebar - Business Profile & Settings
with st.sidebar:
    st.header("🏢 Business Profile")
    biz_name = st.text_input("Business Name", value="WNY Restoration General Contracting LLC")
    phone = st.text_input("Emergency Phone Number", value="(716) 555-0199")
    primary_city = st.text_input("Primary City / Region", value="Buffalo, NY")
    service_areas = st.text_area("Target Towns (comma-separated)", 
                                 value="Buffalo, Amherst, Cheektowaga, Tonawanda, West Seneca, Orchard Park, Clarence, Niagara Falls")
    
    st.divider()
    st.write("💡 **Ranking Tip**: Emergency services convert best when your phone number and 24/7 availability are visible above the fold.")

# Core Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "🎯 SEO Landing Page Builder", 
    "🏷️ Google Schema Generator", 
    "📍 Google Maps / GBP Optimizer", 
    "⭐ Review Generation Engine"
])

# TAB 1: Local Landing Page Generator
with tab1:
    st.subheader("Generate Location-Specific SEO Pages")
    st.write("Google ranks pages that directly match high-intent searches like *'mold remediation in Amherst NY'* or *'emergency water extraction Buffalo'*.")
    
    col1, col2 = st.columns(2)
    with col1:
        service = st.selectbox("Primary Service", [
            "Water Damage Restoration & Extraction",
            "Fire & Smoke Damage Restoration",
            "Mold Remediation & Inspection",
            "General Contracting & Remodeling",
            "Emergency Tree Removal & Storm Cleanup"
        ])
    with col2:
        selected_city = st.selectbox("Target Submarket", [c.strip() for c in service_areas.split(",")])

    page_slug = slugify(service, selected_city)
    phone_digits = normalize_phone(phone)
    meta_title = f"{service} in {selected_city}, NY | {biz_name}"
    meta_desc = f"Fast 24/7 emergency {service.lower()} in {selected_city}, NY. Certified local restoration, general contracting, and tree removal. Call {phone} today!"

    st.markdown("#### Page Meta Preview")
    st.info(f"**URL Slug:** `/{page_slug}`\n\n**Meta Title:** {meta_title}\n\n**Meta Description:** {meta_desc}")

    # Generated Page Content
    page_content = f"""# 24/7 {service} in {selected_city}, NY

Are you dealing with an unexpected emergency in **{selected_city}, NY**? **{biz_name}** provides rapid, certified **{service.lower()}**, rebuild contracting, and cleanup services for residential and commercial properties.

📞 **Immediate Response Hotline:** [{phone}](tel:{phone_digits})  
⏱️ **Response Time:** On-site in 60 minutes or less for critical emergencies.

---

### Why Homeowners in {selected_city} Choose {biz_name}
* **Comprehensive Restoration:** From mitigation to final drywall and structural contracting, we handle the job end-to-end.
* **Direct Insurance Billing:** We work directly with all major homeowners insurance carriers to streamline claims.
* **Certified Technicians:** Advanced moisture-mapping, industrial dehumidification, structural drying, and hazardous tree management.
* **Full-Service General Contracting:** Once damaged materials are removed, our master contracting crew restores your space to pristine condition.

---

### Our Step-by-Step {service} Process
1. **Immediate Assessment & Containment:** Halting further damage, water extraction, or storm-damaged tree stabilization.
2. **Sanitization & Air Scrubbing:** Commercial-grade antimicrobial treatments and HEPA filtration.
3. **Drying & Structural Verification:** Calibrated moisture readings to guarantee zero residual mold or structural rot risk.
4. **General Contracting & Rebuild:** Flooring, framing, drywall, and finish carpentry to return your home to pre-loss condition.

---
### Frequently Asked Questions in {selected_city}

**How fast can your crew arrive on-site in {selected_city}?**  
Our dispatch team maintains 24/7 on-call trucks serving the entire Western New York corridor, typically arriving within 45 to 60 minutes.

**Do you handle tree removal after wind or ice storms?**  
Yes. We deploy bucket trucks, cranes, and chainsaws for fallen or precarious trees threatening roofs, powerlines, and structures.

**Do I have to use the contractor my insurance company assigns?**  
No. In New York, property owners have the legal right to hire any licensed and insured restoration contractor of their choice.
"""
    st.text_area("Generated SEO Markdown (Paste into your WordPress, Squarespace, or Webflow CMS):", value=page_content, height=320)

# TAB 2: Schema Generator
with tab2:
    st.subheader("Google Rich Snippet (JSON-LD) Schema")
    st.write("Embed this code into your website's `<head>` tag. This explicitly tells Google's search crawlers your service radius, business type, and 24/7 status.")

    schema_data = build_schema(biz_name, phone_digits, primary_city, service_areas)

    schema_json = json.dumps(schema_data, indent=2)
    st.code(f'<script type="application/ld+json">\n{schema_json}\n</script>', language="html")

# TAB 3: Google Business Profile (GBP) Posts
with tab3:
    st.subheader("Weekly Google Business Profile Content")
    st.write("Posting regular updates directly on your Google Maps listing sends freshness signals to Google's ranking algorithm.")
    
    topic = st.radio("Select Post Type", ["Emergency Storm Alert", "Mold Prevention Tip", "Recent Project Showcase"])
    
    if topic == "Emergency Storm Alert":
        post_text = f"🚨 Heavy storms passing through Western New York? High winds and torrential rain cause basement flooding and fallen trees. {biz_name} is on standby 24/7 across {primary_city} with water extraction units and tree removal crews. Call {phone} immediately for dispatch."
    elif topic == "Mold Prevention Tip":
        post_text = f"💧 Musty smell in your basement or behind bathroom drywall? Mold spreads within 24–48 hours of moisture intrusion. Our certified inspectors locate hidden leaks using infrared cameras. Protect your family's health—call {biz_name} at {phone}."
    else:
        post_text = f"🔨 Full kitchen & living room rebuild completed! Following a burst pipe incident, our restoration team dried the structure, and our general contracting crew installed new subfloors, cabinets, and drywall. From disaster to dream home—call {biz_name} at {phone}."

    st.text_area("Copy & Paste into Google Business Profile Updates:", value=post_text, height=120)

# TAB 4: Review Request Automation
with tab4:
    st.subheader("5-Star Review Generator")
    st.write("Google's Map 3-pack heavily weights recent, keyword-rich customer reviews mentioning specific services and cities.")
    
    client_name = st.text_input("Customer Name", value="John")
    completed_job = st.selectbox("Job Completed", ["Water Extraction", "Mold Remediation", "Fire Restoration", "Kitchen Remodel", "Tree Removal"])
    
    sms_template = f"Hi {client_name}, thank you for choosing {biz_name}! If you were satisfied with our rapid {completed_job.lower()} service, could you leave us a quick review on Google? It helps local homeowners find trusted contractors in their time of need: [Insert Your Google Review Link Here]"
    
    st.text_area("SMS / Email Review Request Template:", value=sms_template, height=100)