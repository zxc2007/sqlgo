/*===- TableGen'erated file -------------------------------------*- C++ -*-===*\
|*                                                                            *|
|* Interface Declarations                                                     *|
|*                                                                            *|
|* Automatically generated file, do not edit!                                 *|
|*                                                                            *|
\*===----------------------------------------------------------------------===*/

namespace mlir {
namespace vhlo {
class VersionedOpInterface;
namespace detail {
struct VersionedOpInterfaceInterfaceTraits {
  struct Concept {
    /// The methods defined by the interface.
    mlir::vhlo::Version (*getMinVersion)(const Concept *impl, ::mlir::Operation *);
    mlir::vhlo::Version (*getMaxVersion)(const Concept *impl, ::mlir::Operation *);
  };
  template<typename ConcreteOp>
  class Model : public Concept {
  public:
    using Interface = ::mlir::vhlo::VersionedOpInterface;
    Model() : Concept{getMinVersion, getMaxVersion} {}

    static inline mlir::vhlo::Version getMinVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val);
    static inline mlir::vhlo::Version getMaxVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val);
  };
  template<typename ConcreteOp>
  class FallbackModel : public Concept {
  public:
    using Interface = ::mlir::vhlo::VersionedOpInterface;
    FallbackModel() : Concept{getMinVersion, getMaxVersion} {}

    static inline mlir::vhlo::Version getMinVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val);
    static inline mlir::vhlo::Version getMaxVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val);
  };
  template<typename ConcreteModel, typename ConcreteOp>
  class ExternalModel : public FallbackModel<ConcreteModel> {
  public:
    using ConcreteEntity = ConcreteOp;
  };
};template <typename ConcreteOp>
struct VersionedOpInterfaceTrait;

} // namespace detail
class VersionedOpInterface : public ::mlir::OpInterface<VersionedOpInterface, detail::VersionedOpInterfaceInterfaceTraits> {
public:
  using ::mlir::OpInterface<VersionedOpInterface, detail::VersionedOpInterfaceInterfaceTraits>::OpInterface;
  template <typename ConcreteOp>
  struct Trait : public detail::VersionedOpInterfaceTrait<ConcreteOp> {};
  /// Returns the minimum version of the VHLO dialect an op is supported in.
  mlir::vhlo::Version getMinVersion();
  /// Returns the maximum version (inclusive) of the VHLO dialect an op is supported in.
  mlir::vhlo::Version getMaxVersion();
};
namespace detail {
  template <typename ConcreteOp>
  struct VersionedOpInterfaceTrait : public ::mlir::OpInterface<VersionedOpInterface, detail::VersionedOpInterfaceInterfaceTraits>::Trait<ConcreteOp> {
  };
}// namespace detail
} // namespace vhlo
} // namespace mlir
namespace mlir {
namespace vhlo {
template<typename ConcreteOp>
mlir::vhlo::Version detail::VersionedOpInterfaceInterfaceTraits::Model<ConcreteOp>::getMinVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getMinVersion();
}
template<typename ConcreteOp>
mlir::vhlo::Version detail::VersionedOpInterfaceInterfaceTraits::Model<ConcreteOp>::getMaxVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val) {
  return (llvm::cast<ConcreteOp>(tablegen_opaque_val)).getMaxVersion();
}
template<typename ConcreteOp>
mlir::vhlo::Version detail::VersionedOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getMinVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val) {
  return static_cast<const ConcreteOp *>(impl)->getMinVersion(tablegen_opaque_val);
}
template<typename ConcreteOp>
mlir::vhlo::Version detail::VersionedOpInterfaceInterfaceTraits::FallbackModel<ConcreteOp>::getMaxVersion(const Concept *impl, ::mlir::Operation *tablegen_opaque_val) {
  return static_cast<const ConcreteOp *>(impl)->getMaxVersion(tablegen_opaque_val);
}
} // namespace vhlo
} // namespace mlir