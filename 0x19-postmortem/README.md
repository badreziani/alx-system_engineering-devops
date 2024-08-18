# 0x19. Postmortem

## >>> Issue Summary

    Duration of Outage: The incident began at 11:45 AM and was resolved by 12:45 PM EAT (East African Time).
    Impact: The website was entirely inaccessible, with 100% of users unable to access the service due to the site not listening on port 80.
    Root Cause: The root cause was an incorrect configuration in the Nginx server setup. Specifically, the configuration file in sites-available was not properly linked to sites-enabled, which prevented Nginx from serving the website.

## >>> Timeline

    11:45 AM: The issue was first detected when ALX attempted to access the website and found it unresponsive.
    11:50 AM: Monitoring alerts from ALX confirmed the site was down. The issue was escalated to the engineering team.
    11:55 AM: Initial investigations focused on the Nginx configuration files. The team confirmed that the configuration files had no syntax errors.
    12:10 PM: The team investigated services listening on port 80 and found that Nginx was not actively listening.
    12:15 PM: Further investigation revealed that the configuration file in sites-available had not been linked to sites-enabled.
    12:30 PM: The configuration file was linked correctly, and the Nginx service was restarted to apply the changes.
    12:45 PM: The website was fully restored, and the incident was resolved.

## Root Cause and Resolution

### Root Cause:
    The Nginx server was correctly configured in the sites-available directory, but the configuration was not linked to the sites-enabled directory. This omission meant that the Nginx service was running without an active configuration, causing it not to listen on port 80, which in turn made the website inaccessible.

### Resolution:
    The issue was resolved by creating a symbolic link from the configuration file in sites-available to sites-enabled. Once the link was established, the Nginx service was restarted to apply the configuration, which restored the site’s accessibility.

## Corrective and Preventative Measures

### Improvements and Fixes:

    Ensure that all configuration changes are thoroughly validated and that symbolic links between sites-available and sites-enabled are properly established.
    Implement automated checks to verify that Nginx is correctly configured and listening on the correct ports after any changes are made.

### Task List:

    [ ] Develop a script to automatically verify that the sites-available configurations are linked to sites-enabled.
    [ ] Add a monitoring alert specifically for services not listening on port 80.
    [ ] Implement a checklist for deploying configuration changes to ensure all necessary steps are completed.
    [ ] Schedule training sessions for the engineering team on best practices for Nginx configuration management.

## This postmortem serves as a detailed record of the incident, ensuring that similar issues are prevented in the future by implementing the corrective actions listed above.
