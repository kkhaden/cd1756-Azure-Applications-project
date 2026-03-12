# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*

### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

### Option 1: Azure Virtual Machine (VM)

**Cost**
- Usually higher total cost for this type of app.
- You pay for a full VM continuously (compute, disk, networking), even when traffic is low.
- Extra operational cost in time: patching OS, managing web server/process manager, security updates.

**Scalability**
- Manual scaling is possible (resize VM vertically).
- Horizontal scaling is more complex and usually requires additional setup (load balancer, multiple VMs, image management).
- Not ideal for quick, simple scaling needs of a small Flask CMS.

**Availability**
- Availability depends heavily on how the VM is configured.
- To get high availability, additional architecture is needed (multiple VMs/availability zones/load balancer), which increases cost and complexity.
- Single VM can be a single point of failure.

**Workflow**
- Full control over OS and runtime.
- More DevOps overhead: provisioning, hardening, monitoring, patching, process supervision.
- Slower deployment cycle for student projects and small web apps.

---

### Option 2: Azure App Service

**Cost**
- Lower operational overhead and often lower effective cost for a small-to-medium web app.
- Multiple pricing tiers let you start small and scale later.
- Platform-managed infrastructure reduces admin effort.

**Scalability**
- Built-in scaling (vertical and horizontal) with minimal configuration.
- Easier to handle traffic increases compared to VM-based setup.
- Autoscale support (tier-dependent) fits web workloads well.

**Availability**
- Platform provides managed reliability features and easier production-grade setup.
- No OS patch management burden for the app owner.
- Better default availability posture for this project.

**Workflow**
- Faster deployments from local Git/GitHub/Azure tooling.
- Built-in logs, app settings, and monitoring integrations.
- Best fit for Flask app hosting where focus is application features (auth, storage, DB), not infrastructure maintenance.

---

## Chosen option: **Azure App Service** and Justification

I would deploy the CMS app to **Azure App Service**.

This project is a standard Flask web app with Azure SQL + Blob Storage and Microsoft login integration. Therefore an App Service is the better match because it reduces infrastructure management, improved deployment speed, supports scaling and reliability, and aligns with project goals. For this assignment, App Service provides the best balance of cost, maintainability, and delivery speed.
---

## Assess app changes that would change your decision.

I would consider switching to a VM-based deployment if the app requirements changed to include Custom OS-level dependencies or speical networking or security constraints. This is because they are not supported well in App Service runtime/container model, and require deep host/network control. Also if the requirements needed background services/agents, it would make more sense to switch to a VM-based deployment. In full, if the app evolved from a typical managed web workload into a system requiring full infrastructure control, a VM would become more appropriate.