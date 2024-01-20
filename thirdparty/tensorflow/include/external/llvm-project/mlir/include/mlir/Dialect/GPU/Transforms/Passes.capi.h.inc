
/* Autogenerated by mlir-tblgen; don't manually edit. */

#include "mlir-c/Pass.h"

#ifdef __cplusplus
extern "C" {
#endif

// Registration for the entire group
MLIR_CAPI_EXPORTED void mlirRegisterGPUPasses(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuAsyncRegionPass(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuAsyncRegionPass(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuDecomposeMemrefsPass(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuDecomposeMemrefsPass(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuKernelOutlining(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuKernelOutlining(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuLaunchSinkIndexComputations(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuLaunchSinkIndexComputations(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuMapParallelLoopsPass(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuMapParallelLoopsPass(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuModuleToBinaryPass(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuModuleToBinaryPass(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuNVVMAttachTarget(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuNVVMAttachTarget(void);


/* Create GPU Pass. */
MLIR_CAPI_EXPORTED MlirPass mlirCreateGPUGpuROCDLAttachTarget(void);
MLIR_CAPI_EXPORTED void mlirRegisterGPUGpuROCDLAttachTarget(void);



#ifdef __cplusplus
}
#endif