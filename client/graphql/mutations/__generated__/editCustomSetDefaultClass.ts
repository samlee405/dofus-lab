/* tslint:disable */
/* eslint-disable */
// @generated
// This file was automatically generated and should not be edited.

// ====================================================
// GraphQL mutation operation: editCustomSetDefaultClass
// ====================================================

export interface editCustomSetDefaultClass_editCustomSetDefaultClass_customSet_defaultClass {
  __typename: "Class";
  id: any;
  name: string;
  faceImageUrl: string;
  maleSpriteImageUrl: string;
}

export interface editCustomSetDefaultClass_editCustomSetDefaultClass_customSet {
  __typename: "CustomSet";
  id: any;
  lastModified: any | null;
  defaultClass: editCustomSetDefaultClass_editCustomSetDefaultClass_customSet_defaultClass | null;
}

export interface editCustomSetDefaultClass_editCustomSetDefaultClass {
  __typename: "EditCustomSetDefaultClass";
  customSet: editCustomSetDefaultClass_editCustomSetDefaultClass_customSet;
}

export interface editCustomSetDefaultClass {
  editCustomSetDefaultClass: editCustomSetDefaultClass_editCustomSetDefaultClass | null;
}

export interface editCustomSetDefaultClassVariables {
  customSetId?: any | null;
  defaultClassId?: any | null;
}