## Wazuh and DefectDojo Integration

This project provides a simple integration between Wazuh and DefectDojo. Follow the steps below to set up the integration:

1. **Update settings.py file:**
   - Navigate to the `settings.py` file in your project directory.
   - Make the necessary changes according to your DefectDojo setup. 

2. **Modify scanData:**
   - Adjust the scanData parameters as per your requirements. This includes specifying relevant information such as URLs, credentials, etc.

3. **Update engagement_name in defectdojo.py:**
   - Inside the `defectdojo.py` file, locate the `scanData` object.
   - Change the `engagement_name` parameter to match your DefectDojo engagement name. If you don't have one, you can create a new engagement named 'wazuh'.

4. **Update product_name in defectdojo.py:**
   - Still inside the `defectdojo.py` file, locate the `scanData` object.
   - Modify the `product_name` parameter to match your DefectDojo project name. If you haven't created one, you can use 'test' as a placeholder or create a new project.

5. **Save and Execute:**
   - Save all changes made to the files.
   - Execute the integration script to initiate the connection between Wazuh and DefectDojo.

Please make sure to review and test the integration thoroughly after making these changes.
