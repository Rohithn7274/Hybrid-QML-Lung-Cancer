import streamlit as st


def configure_page():
    st.set_page_config(
        page_title="Hybrid Quantum-Classical Lung Cancer Detection System",
        page_icon="🫁",
        layout="wide",
        initial_sidebar_state="expanded",
    )


def render_sidebar():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/000000/lung.png", width=80)
        st.title("Navigation")

        page = st.radio(
            "Select Page",
            [
                "Dashboard",
                "Image Analysis",
                "Patient & Symptom Assessment",
                "Hybrid Quantum-Classical Model",
                "Model Comparison",
                "Explainable AI",
                "Final Results",
                "About Project",
            ],
            label_visibility="collapsed",
        )

        st.divider()

        st.caption("Hybrid Quantum-Classical Lung Cancer Detection")
        st.caption("Version 0.1.0 - Prototype")

        return page


def render_disclaimer():
    st.warning(
        "⚠️ **Disclaimer:** This application is a research prototype and is not intended "
        "to provide medical diagnosis or treatment advice. Please consult a qualified "
        "healthcare professional for medical concerns."
    )


def render_dashboard():
    st.header("📊 Dashboard Overview")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.metric(label="Patients Assessed", value="0", delta="0")
    with col2:
        st.metric(label="Images Analyzed", value="0", delta="0")
    with col3:
        st.metric(label="Classical ML Accuracy", value="—", delta="—")
    with col4:
        st.metric(label="VQC Accuracy", value="—", delta="—")
    with col5:
        st.metric(label="Model Agreement", value="—", delta="—")

    st.divider()

    st.subheader("System Architecture Workflow")

    with st.container():
        col_left, col_right = st.columns(2)

        with col_left:
            st.markdown("**Image Pipeline**")
            st.markdown("""
            CT Scan / X-ray → Upload → Preprocessing → Lung Segmentation → DenseNet-121 → 1024-D Feature Vector → Classical Head + VQC → Output Fusion → Final Prediction
            """)

        with col_right:
            st.markdown("**Symptom Pipeline**")
            st.markdown("""
            Patient Demographics & Symptoms → XGBoost Risk Model → Symptom Risk Score → SHAP Explainability
            """)

    st.divider()

    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Recent Image Analyses")
        st.info("Image analysis history will appear here after analyses are performed.")

    with col_right:
        st.subheader("Recent Symptom Assessments")
        st.info("Patient assessment history will appear here after assessments are performed.")


def render_image_analysis():
    st.header("🖼️ Image Analysis")
    st.markdown("Upload CT scans or X-ray images for lung cancer analysis.")

    st.subheader("Image Upload")

    uploaded_file = st.file_uploader(
        "Choose a CT scan or X-ray image",
        type=["png", "jpg", "jpeg"],
        help="Supported formats: PNG, JPG, JPEG"
    )

    if uploaded_file is not None:
        col1, col2 = st.columns([1, 2])

        with col1:
            st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        with col2:
            st.subheader("Image Information")
            st.write(f"**Filename:** {uploaded_file.name}")
            st.write(f"**File size:** {uploaded_file.size / 1024:.1f} KB")
            st.write(f"**File type:** {uploaded_file.type}")

    st.divider()

    st.subheader("Image Analysis Pipeline")

    pipeline_stages = [
        ("📤", "Image Upload", "Upload CT scan or X-ray"),
        ("⚙️", "Preprocessing", "Normalization, resizing, augmentation"),
        ("🫁", "Lung Segmentation", "Isolate lung regions from background"),
        ("🧠", "DenseNet-121 Feature Extraction", "Extract 1024-dimensional feature vector"),
        ("📊", "Classical Classification Head", "Traditional ML classifier on features"),
        ("⚛️", "Quantum VQC Classification Head", "Variational Quantum Classifier"),
        ("🔀", "Output Fusion", "Combine classical and quantum outputs"),
        ("🎯", "Final Cancer Prediction", "Cancer / No Cancer with probability"),
    ]

    for icon, stage, desc in pipeline_stages:
        with st.expander(f"{icon} {stage}"):
            st.write(desc)
            if stage != "Image Upload":
                st.caption("Not implemented yet — placeholder stage")

    st.divider()

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

    with col_btn2:
        run_clicked = st.button(
            "Run Image Analysis",
            type="primary",
            use_container_width=True,
            disabled=uploaded_file is None,
        )

    if run_clicked:
        st.info(
            "🚧 **Image Analysis Not Yet Connected**\n\n"
            "The image preprocessing, DenseNet-121 feature extraction, "
            "classical ML head, VQC head, and output fusion will be connected "
            "in a later development stage."
        )


def render_patient_symptom_assessment():
    st.header("👤 Patient & Symptom Assessment")
    st.markdown("Enter patient demographic data and clinical symptoms for risk assessment.")

    with st.container():
        st.subheader("Patient Information")

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            age = st.number_input("Age", min_value=1, max_value=120, value=50, step=1)
        with col2:
            gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        with col3:
            smoking = st.selectbox("Smoking History", ["Never Smoked", "Former Smoker", "Current Smoker"])
        with col4:
            years_smoking = st.number_input("Years of Smoking", min_value=0, max_value=80, value=0, step=1)

    st.divider()

    with st.container():
        st.subheader("Clinical Symptoms")

        col1, col2 = st.columns(2)

        with col1:
            persistent_cough = st.checkbox("Persistent Cough")
            hemoptysis = st.checkbox("Hemoptysis / Coughing Blood")
            chest_pain = st.checkbox("Chest Pain")
            shortness_of_breath = st.checkbox("Shortness of Breath")
            wheezing = st.checkbox("Wheezing")

        with col2:
            weight_loss = st.checkbox("Unexplained Weight Loss")
            fatigue = st.checkbox("Fatigue")
            resp_infections = st.checkbox("Recurring Respiratory Infections")
            hoarseness = st.checkbox("Hoarseness")
            dysphagia = st.checkbox("Difficulty Swallowing")

    st.divider()

    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])

    with col_btn2:
        analyze_clicked = st.button(
            "Analyze Symptoms",
            type="primary",
            use_container_width=True,
        )

    if analyze_clicked:
        st.info(
            "🚧 **Symptom Analysis Not Yet Connected**\n\n"
            "The XGBoost symptom risk model and SHAP explainability will be connected "
            "in a later development stage."
        )

    st.divider()

    st.subheader("Symptom Analysis Pipeline")

    pipeline_stages = [
        ("📋", "Patient Demographics & Symptoms", "Age, gender, smoking history, 10 symptoms"),
        ("🌲", "XGBoost Symptom Risk Model", "Gradient-boosted trees for risk scoring"),
        ("📈", "Symptom Risk Score", "Probability output [0, 1]"),
        ("🔍", "SHAP Explainability", "Feature importance and SHAP values"),
    ]

    for icon, stage, desc in pipeline_stages:
        with st.expander(f"{icon} {stage}"):
            st.write(desc)
            if stage != "Patient Demographics & Symptoms":
                st.caption("Not implemented yet — placeholder stage")


def render_hybrid_model():
    st.header("⚛️ Hybrid Quantum-Classical Model Architecture")
    st.markdown("Visual representation of the hybrid quantum-classical classification pipeline.")

    st.subheader("End-to-End Architecture")

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col2:
            st.markdown("""
            ```
            ┌─────────────────────────────────────────────────────────────┐
            │                    INPUT IMAGE                              │
            │                 (CT Scan / X-ray)                           │
            └─────────────────────────┬───────────────────────────────────┘
                                      ▼
            ┌─────────────────────────────────────────────────────────────┐
            │              PREPROCESSING & SEGMENTATION                   │
            │          (Normalization, Resize, Lung Mask)                 │
            └─────────────────────────┬───────────────────────────────────┘
                                      ▼
            ┌─────────────────────────────────────────────────────────────┐
            │                    DenseNet-121                             │
            │         (Pre-trained on ImageNet, fine-tuned)               │
            └─────────────────────────┬───────────────────────────────────┘
                                      ▼
            ┌─────────────────────────────────────────────────────────────┐
            │              1024-DIMENSIONAL FEATURE VECTOR                │
            └─────────────────────────┬───────────────────────────────────┘
                                      ▼
            ┌─────────────────────────┴───────────────────────────────────┐
            │                         SPLIT                                │
            └─────────────────────────┬───────────────────────────────────┘
                                      ▼
            ┌─────────────────────────┼───────────────────────────────────┐
            ▼                         ▼                                   ▼
        ┌─────────┐             ┌───────────┐                        ┌─────────┐
        │ CLASSICAL│            │  QUANTUM  │                        │ FUSION  │
        │  HEAD   │             │   HEAD    │                        │         │
        │         │             │           │                        │         │
        │ Dense   │             │ Feature   │                        │ Weighted│
        │ Layers  │             │ Reduction │                        │ Average │
        │         │             │    ↓      │                        │         │
        │         │             │   VQC     │                        │         │
        └────┬────┘             └─────┬─────┘                        └────┬────┘
             │                        │                                   │
             ▼                        ▼                                   ▼
        ┌─────────┐             ┌───────────┐                        ┌─────────┐
        │CLASSICAL│             │  QUANTUM  │                        │  FINAL  │
        │ OUTPUT  │             │  OUTPUT   │                        │PREDICTION│
        │ P(class)│             │ P(class)  │                        │ P(cancer)│
        └─────────┘             └───────────┘                        └─────────┘
            ```
            """)

    st.divider()

    st.subheader("Component Details")

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "DenseNet-121",
        "Classical Head",
        "Quantum Head (VQC)",
        "Output Fusion",
        "Feature Vector",
    ])

    with tab1:
        st.markdown("**DenseNet-121 Feature Extractor**")
        st.write("• Pre-trained on ImageNet, fine-tuned on lung CT/X-ray dataset")
        st.write("• Output: 1024-dimensional feature vector from global average pooling layer")
        st.write("• Frozen backbone with trainable final dense layers")
        st.write("• Transfer learning for medical imaging domain adaptation")
        st.info("Not implemented yet — placeholder component")

    with tab2:
        st.markdown("**Classical Classification Head**")
        st.write("• Input: 1024-D feature vector")
        st.write("• Architecture: Dense(512) → ReLU → Dropout(0.3) → Dense(256) → ReLU → Dense(1)")
        st.write("• Output: Cancer probability [0, 1] via sigmoid")
        st.write("• Loss: Binary cross-entropy")
        st.info("Not implemented yet — placeholder component")

    with tab3:
        st.markdown("**Quantum Variational Classifier (VQC)**")
        st.write("• Input: Reduced feature vector (1024 → 8-10 dimensions via PCA/autoencoder)")
        st.write("• Feature Map: Angle encoding or amplitude encoding")
        st.write("• Ansatz: Hardware-efficient / strongly entangling layers")
        st.write("• Qubits: 8-10 (matching reduced feature dimension)")
        st.write("• Layers: 3-4 variational layers")
        st.write("• Optimizer: COBYLA / SPSA / Adam")
        st.write("• Shots: 1024 (simulator) / Hardware execution on IBM Quantum")
        st.write("• Output: Cancer probability [0, 1]")
        st.info("Not implemented yet — placeholder component")

    with tab4:
        st.markdown("**Output Fusion Strategy**")
        st.write("• Method: Weighted average of classical and quantum probabilities")
        st.write("• Weights: Learned via validation set optimization (or fixed 0.5/0.5)")
        st.write("• Alternative: Meta-learner (logistic regression on both outputs)")
        st.write("• Calibration: Temperature scaling for probability calibration")
        st.info("Not implemented yet — placeholder component")

    with tab5:
        st.markdown("**1024-D Feature Vector**")
        st.write("• Extracted from DenseNet-121 global average pooling layer")
        st.write("• Represents high-level visual features of lung tissue")
        st.write("• Used as input to both classical and quantum heads")
        st.write("• For quantum head: dimensionality reduction to 8-10 dimensions")
        st.info("Not implemented yet — placeholder component")


def render_model_comparison():
    st.header("⚖️ Model Comparison")
    st.markdown("Side-by-side comparison of Classical ML and VQC performance metrics.")

    st.info("Real metric values will be populated after model training and evaluation.")

    st.subheader("Performance Metrics Comparison")

    metrics_data = {
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall (Sensitivity)",
            "Specificity",
            "F1 Score",
            "ROC-AUC",
            "Inference Time (ms)",
            "Parameters",
        ],
        "Classical ML": ["—", "—", "—", "—", "—", "—", "—", "—"],
        "VQC": ["—", "—", "—", "—", "—", "—", "—", "—"],
        "Hybrid (Fused)": ["—", "—", "—", "—", "—", "—", "—", "—"],
    }

    st.table(metrics_data)

    st.divider()

    st.subheader("Detailed Comparison")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Classical ML Configuration**")
        with st.expander("Model Details"):
            st.write("• Algorithm: TBD (Random Forest / XGBoost / SVM / DenseNet Head)")
            st.write("• Feature Input: 1024-D DenseNet features")
            st.write("• Hyperparameters: To be optimized via cross-validation")
            st.write("• Training: Standard classical optimization")

        with st.expander("Expected Advantages"):
            st.write("• Fast inference on CPU/GPU")
            st.write("• Mature, well-understood algorithms")
            st.write("• Easy deployment and interpretability")

    with col2:
        st.markdown("**VQC Configuration**")
        with st.expander("Model Details"):
            st.write("• Framework: PennyLane / Qiskit")
            st.write("• Qubits: 8-10")
            st.write("• Ansatz: Hardware-efficient / Strongly entangling")
            st.write("• Layers: 3-4")
            st.write("• Feature Encoding: Angle / Amplitude")
            st.write("• Optimizer: COBYLA / SPSA / Adam")
            st.write("• Shots: 1024")
            st.write("• Backend: Simulator / IBM Quantum Hardware")

        with st.expander("Expected Advantages"):
            st.write("• Potential quantum advantage on complex boundaries")
            st.write("• High-dimensional feature space exploration")
            st.write("• Novel inductive bias for medical data")

    st.divider()

    st.subheader("Training & Evaluation Plan")
    st.markdown("""
    1. **Data Split**: 70% train / 15% validation / 15% test (stratified)
    2. **Cross-Validation**: 5-fold CV on training set for hyperparameter tuning
    3. **Metrics**: All metrics computed on held-out test set
    4. **Statistical Significance**: McNemar's test for pairwise comparison
    5. **Calibration**: Reliability diagrams and Brier score
    6. **Subgroup Analysis**: Performance by age, gender, smoking status
    """)


def render_explainable_ai():
    st.header("🔍 Explainable AI")
    st.markdown("Interpretability modules for both image and symptom analysis pipelines.")

    tab1, tab2 = st.tabs(["Image Explainability (Grad-CAM)", "Symptom Explainability (SHAP)"])

    with tab1:
        st.subheader("Grad-CAM for Image Analysis")
        st.markdown("Gradient-weighted Class Activation Mapping for DenseNet-121.")

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**Original Image**")
            st.info("Upload an image in the Image Analysis page to enable Grad-CAM visualization.")
            st.empty()

        with col2:
            st.markdown("**Grad-CAM Heatmap Overlay**")
            st.info("Heatmap will highlight regions contributing to cancer prediction.")
            st.empty()

        st.divider()

        st.markdown("**Grad-CAM Configuration (Planned)**")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.selectbox("Target Layer", ["Last Conv Block", "Custom"], disabled=True)
        with col2:
            st.selectbox("Colormap", ["Jet", "Viridis", "Hot", "Cool"], disabled=True)
        with col3:
            st.slider("Overlay Alpha", 0.0, 1.0, 0.5, disabled=True)

        with st.expander("Technical Details"):
            st.write("• Target layer: Last convolutional block of DenseNet-121")
            st.write("• Gradients: ∂y^c/∂A^k (gradients of class score w.r.t. feature maps)")
            st.write("• Weights: α_k^c = GlobalAveragePooling(∂y^c/∂A^k)")
            st.write("• Heatmap: ReLU(Σ_k α_k^c A^k)")
            st.write("• Resolution: Upsampled to input image resolution")

    with tab2:
        st.subheader("SHAP for Symptom Analysis")
        st.markdown("SHapley Additive exPlanations for XGBoost symptom risk model.")

        st.markdown("**Feature Importance Placeholder**")
        st.info("SHAP summary plot (beeswarm) will appear here after model training.")
        st.empty()

        st.divider()

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("**SHAP Summary Plot (Beeswarm)**")
            st.caption("Shows feature impact distribution across patients")

        with col2:
            st.markdown("**SHAP Waterfall Plot**")
            st.caption("Explains individual prediction for selected patient")

        st.divider()

        st.markdown("**SHAP Configuration (Planned)**")
        col1, col2 = st.columns(2)
        with col1:
            st.selectbox("SHAP Explainer Type", ["TreeExplainer (XGBoost)", "KernelExplainer", "PermutationExplainer"], disabled=True)
        with col2:
            st.number_input("Max Samples for KernelExplainer", min_value=100, max_value=10000, value=500, disabled=True)

        with st.expander("Technical Details"):
            st.write("• Explainer: TreeExplainer for XGBoost (exact, fast)")
            st.write("• Features: 14 (4 demographics + 10 symptoms)")
            st.write("• Output: SHAP values per feature per patient")
            st.write("• Global: Mean |SHAP| for feature importance ranking")
            st.write("• Local: Waterfall plot for individual prediction breakdown")


def render_final_results():
    st.header("📋 Final Results Dashboard")
    st.markdown("Consolidated prediction results from all analysis pipelines.")

    st.info("All prediction values are placeholders until models are connected.")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Primary Prediction")

        with st.container(border=True):
            st.metric(
                label="Cancer Prediction",
                value="Model not connected yet",
                delta=None,
            )
            st.metric(
                label="Cancer Probability",
                value="—",
                delta=None,
            )

    with col2:
        st.subheader("Model Outputs")

        with st.container(border=True):
            st.metric(
                label="Classical ML Output",
                value="Model not connected yet",
                delta=None,
            )
            st.metric(
                label="VQC Output",
                value="Model not connected yet",
                delta=None,
            )
            st.metric(
                label="Hybrid / Fused Output",
                value="Model not connected yet",
                delta=None,
            )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Symptom Risk Assessment")

        with st.container(border=True):
            st.metric(
                label="Symptom Risk Score",
                value="Model not connected yet",
                delta=None,
            )
            st.metric(
                label="Risk Category",
                value="—",
                delta=None,
            )

    with col2:
        st.subheader("Explainability Results")

        with st.container(border=True):
            st.metric(
                label="Grad-CAM Result",
                value="Not available",
                delta=None,
            )
            st.metric(
                label="SHAP Important Features",
                value="Not available",
                delta=None,
            )

    st.divider()

    st.subheader("Results Export")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.button("Export PDF Report", disabled=True, use_container_width=True)
    with col2:
        st.button("Export JSON", disabled=True, use_container_width=True)
    with col3:
        st.button("Save to Database", disabled=True, use_container_width=True)

    st.caption("Export functionality will be enabled after model integration.")


def render_about_project():
    st.header("ℹ️ About Project")

    st.markdown("""
    ### Hybrid Quantum-Classical Lung Cancer Detection System

    This research prototype explores the integration of **classical machine learning** 
    with **variational quantum classifiers (VQC)** for early lung cancer detection
    using both medical imaging and clinical symptom data.
    """)

    st.divider()

    st.subheader("Problem Statement")
    st.markdown("""
    Lung cancer remains the leading cause of cancer-related deaths worldwide. 
    Early detection significantly improves survival rates, but current screening 
    methods have limitations:
    - Low-dose CT screening has high false-positive rates
    - Symptom-based assessment is subjective and often delayed
    - Limited integration of imaging and clinical data
    - Classical ML models may miss complex patterns in high-dimensional data
    """)

    st.subheader("Objective")
    st.markdown("""
    Develop a hybrid quantum-classical system that:
    1. **Leverages DenseNet-121** for robust feature extraction from CT/X-ray images
    2. **Employs XGBoost** for symptom-based risk stratification with SHAP explainability
    3. **Implements VQC** to explore potential quantum advantage in classification
    4. **Fuses outputs** from classical and quantum heads for improved prediction
    5. **Provides explainability** via Grad-CAM (images) and SHAP (symptoms)
    """)

    st.subheader("Hybrid Quantum-Classical Approach")
    st.markdown("""
    The core innovation lies in the parallel processing architecture:
    
    **Classical Path**: DenseNet-121 → Dense layers → Probability
    
    **Quantum Path**: DenseNet-121 → Feature Reduction (1024→8-10) → Angle Encoding → VQC → Probability
    
    **Fusion**: Weighted combination or meta-learning for final prediction
    
    This architecture allows direct comparison of classical vs. quantum performance
    on identical feature representations.
    """)

    st.subheader("Image-Based Analysis Pipeline")
    st.markdown("""
    1. **Upload**: CT scan or X-ray (PNG, JPG, JPEG)
    2. **Preprocessing**: Normalization, resizing to 224×224, lung segmentation
    3. **Feature Extraction**: DenseNet-121 (pre-trained, fine-tuned) → 1024-D vector
    4. **Classical Head**: Dense layers for classification
    5. **Quantum Head**: PCA/autoencoder reduction → VQC
    6. **Fusion**: Combined probability output
    7. **Explainability**: Grad-CAM heatmap on original image
    """)

    st.subheader("Symptom-Based Risk Analysis Pipeline")
    st.markdown("""
    1. **Input**: 4 demographics + 10 clinical symptoms
    2. **Model**: XGBoost gradient-boosted trees
    3. **Output**: Risk probability score [0, 1]
    4. **Explainability**: SHAP values (global + local)
    5. **Risk Categories**: Low (<0.33), Moderate (0.33-0.66), High (>0.66)
    """)

    st.subheader("Classical ML vs VQC Comparison")
    st.markdown("""
    | Aspect | Classical ML | VQC |
    |--------|--------------|-----|
    | **Inference Speed** | Fast (ms) | Slower (quantum circuit execution) |
    | **Hardware** | CPU/GPU | Quantum simulator / NISQ hardware |
    | **Interpretability** | SHAP, feature importance | Parameter analysis, gradient-based |
    | **Scalability** | Excellent | Limited by qubit count/noise |
    | **Potential Advantage** | Proven on tabular/image data | High-dimensional feature spaces |
    """)

    st.subheader("Explainable AI Integration")
    st.markdown("""
    - **Grad-CAM**: Visual localization of cancer-relevant regions in CT/X-ray
    - **SHAP**: Feature attribution for symptom-based risk factors
    - **Quantum Interpretability**: Circuit parameter sensitivity, entanglement analysis
    - **Clinical Alignment**: Validate explanations against radiologist annotations
    """)

    st.subheader("Planned FastAPI Backend")
    st.markdown("""
    Future migration to a production-ready backend:
    - **FastAPI** for high-performance async API
    - **Model Serving**: ONNX Runtime / TorchServe for classical, PennyLane Lightning for VQC
    - **Queue System**: Celery + Redis for async inference
    - **Database**: PostgreSQL for patient records, results, audit logs
    - **Authentication**: OAuth2/JWT for clinical access control
    - **Monitoring**: Prometheus + Grafana for metrics
    """)

    st.subheader("Current Streamlit Prototype")
    st.markdown("""
    This Streamlit application serves as:
    - **UI/UX validation** for clinical workflow
    - **Architecture visualization** for stakeholder communication
    - **Integration testing** platform for model components
    - **Demonstration** of hybrid quantum-classical concept
    
    **Status**: UI prototype only — no ML models connected yet.
    """)

    st.divider()

    st.caption("Hybrid Quantum-Classical Lung Cancer Detection System — Research Prototype v0.1.0")


def main():
    configure_page()

    st.title("🫁 Hybrid Quantum-Classical Lung Cancer Detection System")

    page = render_sidebar()

    render_disclaimer()

    if page == "Dashboard":
        render_dashboard()
    elif page == "Image Analysis":
        render_image_analysis()
    elif page == "Patient & Symptom Assessment":
        render_patient_symptom_assessment()
    elif page == "Hybrid Quantum-Classical Model":
        render_hybrid_model()
    elif page == "Model Comparison":
        render_model_comparison()
    elif page == "Explainable AI":
        render_explainable_ai()
    elif page == "Final Results":
        render_final_results()
    elif page == "About Project":
        render_about_project()


if __name__ == "__main__":
    main()