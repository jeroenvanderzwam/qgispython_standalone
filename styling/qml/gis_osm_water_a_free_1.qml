<!DOCTYPE qgis PUBLIC 'http://mrcc.com/qgis.dtd' 'SYSTEM'>
<qgis hasScaleBasedVisibilityFlag="0" simplifyDrawingTol="1" styleCategories="AllStyleCategories" simplifyAlgorithm="0" simplifyDrawingHints="1" simplifyLocal="1" minScale="1e+08" readOnly="0" simplifyMaxScale="1" version="3.10.0-A Coruña" maxScale="0" labelsEnabled="0">
  <flags>
    <Identifiable>1</Identifiable>
    <Removable>1</Removable>
    <Searchable>1</Searchable>
  </flags>
  <renderer-v2 symbollevels="0" type="singleSymbol" forceraster="0" enableorderby="0">
    <symbols>
      <symbol clip_to_extent="1" type="fill" force_rhr="0" alpha="1" name="0">
        <layer pass="0" enabled="1" class="SimpleFill" locked="0">
          <prop k="border_width_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="color" v="184,217,247,255"/>
          <prop k="joinstyle" v="bevel"/>
          <prop k="offset" v="0,0"/>
          <prop k="offset_map_unit_scale" v="3x:0,0,0,0,0,0"/>
          <prop k="offset_unit" v="MM"/>
          <prop k="outline_color" v="0,0,0,255"/>
          <prop k="outline_style" v="no"/>
          <prop k="outline_width" v="0.26"/>
          <prop k="outline_width_unit" v="MM"/>
          <prop k="style" v="solid"/>
          <data_defined_properties>
            <Option type="Map">
              <Option type="QString" value="" name="name"/>
              <Option name="properties"/>
              <Option type="QString" value="collection" name="type"/>
            </Option>
          </data_defined_properties>
        </layer>
      </symbol>
    </symbols>
    <rotation/>
    <sizescale/>
  </renderer-v2>
  <customproperties>
    <property key="embeddedWidgets/count" value="0"/>
    <property key="variableNames"/>
    <property key="variableValues"/>
  </customproperties>
  <blendMode>0</blendMode>
  <featureBlendMode>0</featureBlendMode>
  <layerOpacity>1</layerOpacity>
  <SingleCategoryDiagramRenderer attributeLegend="1" diagramType="Histogram">
    <DiagramCategory diagramOrientation="Up" maxScaleDenominator="1e+08" height="15" scaleBasedVisibility="0" barWidth="5" labelPlacementMethod="XHeight" minScaleDenominator="0" enabled="0" minimumSize="0" penColor="#000000" penWidth="0" backgroundAlpha="255" lineSizeType="MM" width="15" opacity="1" scaleDependency="Area" rotationOffset="270" lineSizeScale="3x:0,0,0,0,0,0" backgroundColor="#ffffff" sizeType="MM" sizeScale="3x:0,0,0,0,0,0" penAlpha="255">
      <fontProperties description="MS Shell Dlg 2,8.25,-1,5,50,0,0,0,0,0" style=""/>
      <attribute field="" label="" color="#000000"/>
    </DiagramCategory>
  </SingleCategoryDiagramRenderer>
  <DiagramLayerSettings dist="0" obstacle="0" linePlacementFlags="18" priority="0" showAll="1" placement="1" zIndex="0">
    <properties>
      <Option type="Map">
        <Option type="QString" value="" name="name"/>
        <Option name="properties"/>
        <Option type="QString" value="collection" name="type"/>
      </Option>
    </properties>
  </DiagramLayerSettings>
  <geometryOptions geometryPrecision="0" removeDuplicateNodes="0">
    <activeChecks/>
    <checkConfiguration/>
  </geometryOptions>
  <fieldConfiguration>
    <field name="fid">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="osm_id">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="code">
      <editWidget type="Range">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="fclass">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
    <field name="name">
      <editWidget type="TextEdit">
        <config>
          <Option/>
        </config>
      </editWidget>
    </field>
  </fieldConfiguration>
  <aliases>
    <alias field="fid" index="0" name=""/>
    <alias field="osm_id" index="1" name=""/>
    <alias field="code" index="2" name=""/>
    <alias field="fclass" index="3" name=""/>
    <alias field="name" index="4" name=""/>
  </aliases>
  <excludeAttributesWMS/>
  <excludeAttributesWFS/>
  <defaults>
    <default field="fid" applyOnUpdate="0" expression=""/>
    <default field="osm_id" applyOnUpdate="0" expression=""/>
    <default field="code" applyOnUpdate="0" expression=""/>
    <default field="fclass" applyOnUpdate="0" expression=""/>
    <default field="name" applyOnUpdate="0" expression=""/>
  </defaults>
  <constraints>
    <constraint exp_strength="0" field="fid" notnull_strength="1" unique_strength="1" constraints="3"/>
    <constraint exp_strength="0" field="osm_id" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="code" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="fclass" notnull_strength="0" unique_strength="0" constraints="0"/>
    <constraint exp_strength="0" field="name" notnull_strength="0" unique_strength="0" constraints="0"/>
  </constraints>
  <constraintExpressions>
    <constraint field="fid" exp="" desc=""/>
    <constraint field="osm_id" exp="" desc=""/>
    <constraint field="code" exp="" desc=""/>
    <constraint field="fclass" exp="" desc=""/>
    <constraint field="name" exp="" desc=""/>
  </constraintExpressions>
  <expressionfields/>
  <attributeactions>
    <defaultAction key="Canvas" value="{00000000-0000-0000-0000-000000000000}"/>
  </attributeactions>
  <attributetableconfig sortExpression="" actionWidgetStyle="dropDown" sortOrder="0">
    <columns>
      <column hidden="0" type="field" width="-1" name="osm_id"/>
      <column hidden="0" type="field" width="-1" name="code"/>
      <column hidden="0" type="field" width="-1" name="fclass"/>
      <column hidden="0" type="field" width="-1" name="name"/>
      <column hidden="1" type="actions" width="-1"/>
      <column hidden="0" type="field" width="-1" name="fid"/>
    </columns>
  </attributetableconfig>
  <conditionalstyles>
    <rowstyles/>
    <fieldstyles/>
  </conditionalstyles>
  <storedexpressions/>
  <editform tolerant="1">D:/Gebruikers/peter/Bureaublad/osm</editform>
  <editforminit/>
  <editforminitcodesource>0</editforminitcodesource>
  <editforminitfilepath>D:/Gebruikers/peter/Bureaublad/osm</editforminitfilepath>
  <editforminitcode><![CDATA[# -*- coding: utf-8 -*-
"""
Les formulaires QGIS peuvent avoir une fonction Python qui sera appelée à l'ouverture du formulaire.

Utilisez cette fonction pour ajouter plus de fonctionnalités à vos formulaires.

Entrez le nom de la fonction dans le champ "Fonction d'initialisation Python".
Voici un exemple à suivre:
"""
from qgis.PyQt.QtWidgets import QWidget

def my_form_open(dialog, layer, feature):
    geom = feature.geometry()
    control = dialog.findChild(QWidget, "MyLineEdit")

]]></editforminitcode>
  <featformsuppress>0</featformsuppress>
  <editorlayout>generatedlayout</editorlayout>
  <editable>
    <field editable="1" name="code"/>
    <field editable="1" name="fclass"/>
    <field editable="1" name="fid"/>
    <field editable="1" name="name"/>
    <field editable="1" name="osm_id"/>
  </editable>
  <labelOnTop>
    <field name="code" labelOnTop="0"/>
    <field name="fclass" labelOnTop="0"/>
    <field name="fid" labelOnTop="0"/>
    <field name="name" labelOnTop="0"/>
    <field name="osm_id" labelOnTop="0"/>
  </labelOnTop>
  <widgets/>
  <previewExpression>name</previewExpression>
  <mapTip></mapTip>
  <layerGeometryType>2</layerGeometryType>
</qgis>
