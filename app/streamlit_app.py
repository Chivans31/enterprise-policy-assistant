import requests
import streamlit as st
import json

st.set_page_config(
    page_title="Enterprise Policy Assistant"
)

st.title("Enterprise Policy Assistant")

question = st.text_input(
    "Ask a question about company policies"
)

if st.button("Submit") and question:

    with requests.post(
        "http://localhost:8000/ask-stream",
        json={"question": question},
        stream=True
    ) as r:

        container = st.empty()

        full_response = ""

        sources = []

        iter_lines = r.iter_lines()

        try:

            # Read metadata
            first_line = next(iter_lines).decode("utf-8")

            if "--END_METADATA--" in first_line:

                metadata_str = first_line.replace(
                    "--END_METADATA--",
                    ""
                )

                sources = json.loads(
                    metadata_str
                ).get("sources", [])

        except StopIteration:

            st.error("No response from server.")

        # Stream answer
        for chunk in iter_lines:

            if chunk:

                full_response += chunk.decode(
                    "utf-8"
                )

                container.markdown(
                    full_response + "▌"
                )

        container.markdown(full_response)

        # Show sources
        if sources:

            st.subheader("Sources")

            for s in sources:

                st.caption(
                    f"{s['source']} (Page {s['page']})"
                )